from sqlmodel.ext.asyncio.session import AsyncSession
from .models import *
from sqlmodel import select

class InventoryOperations():
    
    async def get_products(self, session: AsyncSession):
        statement = select(Products)
        
        result = await session.execute(statement)
        return result.scalars().all()