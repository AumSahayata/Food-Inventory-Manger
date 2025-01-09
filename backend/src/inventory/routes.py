from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.main import get_session
from .schemas import *
from typing import List
from .operations import InventoryOperations

inventory_router = APIRouter()
inventory_ops = InventoryOperations()

@inventory_router.get("/products/{vendor_id}", response_model=List[ProductModel])
async def get_all_products(vendor_id:str, session: AsyncSession = Depends(get_session)):
    
    products = await inventory_ops.get_products(vendor_id, session)
    
    if products:
        return products
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="products not found")

@inventory_router.post("/add/product", status_code = status.HTTP_201_CREATED)
async def add_product(product_data: AddProductModel, session: AsyncSession = Depends(get_session)):
    
    res = await inventory_ops.add_new_product(product_data, session)
    
    if not res:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Cannot add Product.")

@inventory_router.get("/{vendor_id}", response_model=List[InventoryModel])
async def get_all_products(vendor_id:str, session: AsyncSession = Depends(get_session)):
    
    inventory = await inventory_ops.get_inventory(vendor_id, session)
    
    if inventory:
        return inventory
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Inventory not found")

@inventory_router.post("/add", status_code = status.HTTP_201_CREATED)
async def add_inventory(inventory_data: AddInventoryModel, session: AsyncSession = Depends(get_session)):
    
    res = await inventory_ops.add_new_inv(inventory_data, session)
    
    if not res:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Cannot add Inventory.")

@inventory_router.patch("/buy/{product_id}", status_code = status.HTTP_200_OK)
async def buy_product(product_id: str, session: AsyncSession = Depends(get_session)):
    
    res = await inventory_ops.update_on_buy(product_id, session)
    
    if not res:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Cannot purchase the product. Something went wrong!!")

@inventory_router.get("/expiry/{vendor_id}", response_model=List[ExpiryData])
async def get_expity(vendor_id:str, session: AsyncSession = Depends(get_session)):
    
    res = await inventory_ops.get_vendor_expiry(vendor_id, session)
    
    if not res:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No expiry products not found")
    
    return res

@inventory_router.patch("/discount", status_code=status.HTTP_200_OK)
async def make_discounted(discount_data:DiscountData, session: AsyncSession = Depends(get_session)):
    
    res = await inventory_ops.add_discount(discount_data, session)
    
    # if not res:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cannot add discount")