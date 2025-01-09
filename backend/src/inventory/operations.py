from sqlmodel.ext.asyncio.session import AsyncSession
from .models import *
from .schemas import *
from sqlmodel import select, update, insert
from datetime import timedelta 

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
                "expiry_date": row.expiry_date
            }
            for row in rows
        ]
        print(inventory_list)

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
        check_date = check_date + timedelta(days=1)
        
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