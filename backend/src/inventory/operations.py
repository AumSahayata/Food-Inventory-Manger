from sqlmodel.ext.asyncio.session import AsyncSession
from .models import *
from .schemas import *
from sqlmodel import select

class InventoryOperations():
    
    async def get_products(self, vendor_id:str, session: AsyncSession):
        statement = select(Products).where(Products.vendor_id == vendor_id)
        
        result = await session.execute(statement)
        return result.scalars().all()
    
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