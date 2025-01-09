from fastapi import APIRouter, Depends, HTTPException, Request, status
from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.main import get_session
from .schemas import *
from typing import List
from .operations import InventoryOperations

inventory_router = APIRouter()
inventory_ops = InventoryOperations()

@inventory_router.get("/products", response_model=List[ProductModel])
async def get_all_products(session: AsyncSession = Depends(get_session)):
    
    products = await inventory_ops.get_products(session)
    
    if products:
        return products
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="products not found")
    
@inventory_router.post("/add", status_code = status.HTTP_201_CREATED)
async def add_inventory(content_data: ContentCreateModel, session: AsyncSession = Depends(get_session)):