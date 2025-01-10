import datetime
from sqlmodel.ext.asyncio.session import AsyncSession
from .models import *
from .schemas import *
from sqlmodel import select, update, insert, case
from .utils import predict

class InventoryOperations():
    
    async def get_products(self, vendor_id:str, session: AsyncSession):
        statement = select(Products).where(Products.vendor_id == vendor_id)
        
        result = await session.execute(statement)
        return result.scalars().all()
    
    async def get_batch_by_p_id(self, product_id:str, session: AsyncSession):
        statement = select(Inventory).where(Inventory.product_id == product_id).order_by(Inventory.expiry_date)
        
        result = await session.execute(statement)
        return result.scalars().first()
    
    async def add_new_product(self, product_data: AddProductModel, session: AsyncSession):
        product_data_dict = product_data.model_dump()
        
        new_product = Products(
            **product_data_dict
        )
        
        session.add(new_product)
        await session.commit()
        return new_product
    
    async def get_inventory(self, vendor_id:str, session: AsyncSession):
        statement = (select(Products.name,
        Products.category,
        Inventory.product_id,
        Inventory.batch_id,
        Inventory.vendor_id,
        Inventory.quantity,
        Inventory.is_discounted,
        Inventory.discount_percentage,
        Inventory.expiry_date).join(Inventory, Inventory.product_id == Products.p_id).where(Inventory.vendor_id == vendor_id))
        
        result = await session.execute(statement)
        result = await session.execute(statement)
        rows = result.all()

        # Map the results to a list of dictionaries or Pydantic models (if needed)
        inventory_list = [
            {
                "product_name": row.name,
                "product_category": row.category,
                "p_id": row.product_id,
                "batch_id": row.batch_id,
                "vendor_id": row.vendor_id,
                "quantity": row.quantity,
                "is_discounted": row.is_discounted,
                "discount_percentage": row.discount_percentage,
                "expiry_date": row.expiry_date
            }
            for row in rows
        ]

        return inventory_list
    
    async def add_new_inv(self, inventory_data: AddInventoryModel, session: AsyncSession):
        inv_data_dict = inventory_data.model_dump()
        
        new_inv = Inventory(
            **inv_data_dict
        )
        
        session.add(new_inv)
        await session.commit()
        return new_inv
    
    async def update_on_buy(self, product_id: str, session: AsyncSession):
        
        statement = select(Inventory).where(Inventory.product_id == product_id).order_by(Inventory.expiry_date)
        
        result = await session.execute(statement)
        inventory_item = result.scalars().first()
        
        new_quantity = inventory_item.quantity - 1
        
        if not inventory_item:
            return -1
        else:
            update_statement = (update(Inventory).where(Inventory.product_id == product_id, Inventory.batch_id == inventory_item.batch_id).values(quantity=new_quantity))
            await session.execute(update_statement)
            await session.commit()
            
            await self.add_sales(product_id, session)
            
            return inventory_item
        
    async def add_sales(self, product_id: str, session: AsyncSession):
        
        check_date = date.today()        
        sale_statement = select(Sales).where(Sales.product_id == product_id,Sales.sale_date == check_date)
        result = await session.execute(sale_statement)
        existing_sale = result.scalar_one_or_none()
        
        
        if existing_sale:
            new_quantity_sold = existing_sale.quantity_sold + 1
            update_sale_statement = (
                update(Sales).where(Sales.sale_id == existing_sale.sale_id).values(quantity_sold=new_quantity_sold))
            await session.execute(update_sale_statement)
            
        else:
            insert_sale_statement = (insert(Sales).values(
                    product_id=product_id,
                    sale_date=check_date,
                    is_holiday=False,
                    sale_day=check_date.isoweekday(),
                    quantity_sold=1
                )
            )
            await session.execute(insert_sale_statement)
            
        await session.commit()

        return {"message": "Sale recorded successfully"}
    
    
    async def check_and_insert_expiry(self, session: AsyncSession):
        today = date.today()

        # Query to filter products based on the expiry criteria
        statement = (
        select(
            Inventory.batch_id,
            Inventory.product_id,
            Inventory.vendor_id,
            Products.category,
            (Inventory.expiry_date - today).label("days_remaining")
        )
        .join(Products, Inventory.product_id == Products.p_id)
        .where(
            case(
                # Dairy: expiry days <= 2
                (Products.category == "Dairy", (Inventory.expiry_date - today) <= 2),
                # F&V: expiry days <= 1
                (Products.category == "F&V", (Inventory.expiry_date - today) <= 1),
            )
        )
        )

        result = await session.execute(statement)
        expiring_products = result.all()

        # Insert matching records into the Expiry table
        for batch_id, product_id, vendor_id, category, days_remaining in expiring_products:
            insert_statement = (
                insert(Expiry)
                .values(
                    batch_id=batch_id,
                    product_id=product_id,
                    vendor_id=vendor_id,
                    days_remaining=days_remaining,
                    date_added=today
                )
            )
            await session.execute(insert_statement)
            
        await session.commit()

        return {"message": "Expiry table updated"}
    
    
    async def get_vendor_expiry(self, vendor_id:str, session: AsyncSession):
        statement = (
        select(
            Expiry.batch_id,
            Expiry.product_id,
            Expiry.days_remaining,
            Expiry.date_added,
            Products.name.label("product_name")
        )
        .join(Products, Expiry.product_id == Products.p_id)).where(Expiry.vendor_id == vendor_id)

        # Execute the query
        result = await session.execute(statement)

        # Process results
        expiry_data = [
            {
                "batch_id": row.batch_id,
                "product_id": row.product_id,
                "product_name": row.product_name,
                "days_remaining": row.days_remaining,
                "date_added": row.date_added,
            }
            for row in result
        ]
        return expiry_data

    async def add_discount(self, discount_data: DiscountData, session: AsyncSession):
        update_data_dict = discount_data.model_dump()
        
        res = update(Inventory).where(Inventory.batch_id == update_data_dict['batch_id']).values(is_discounted = update_data_dict["is_discounted"], discount_percentage = update_data_dict["discount_percentage"])
        
        await session.execute(res)
        await session.commit()
        
        return res
    
    async def prediction(self, prediction_data: PredictData, session: AsyncSession):
        prediction_data = prediction_data.model_dump()
        month = datetime.datetime.now().month
        prod_cat = await self.get_category(prediction_data["product_id"], session) 
        data = [month, prediction_data["product_name"], prod_cat, date.today().isoweekday(), 0]
        result = predict(data)
        
        return result
    
    async def get_category(self, product_id: str, session: AsyncSession):
        res = select(Products.category).where(Products.p_id==product_id)
        result = await session.execute(res)
        category = result.scalars().first()
        return category