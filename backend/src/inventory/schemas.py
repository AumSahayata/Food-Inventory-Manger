from typing import List
from pydantic import BaseModel
from datetime import date
import uuid

class ProductModel(BaseModel):
    p_id: uuid.UUID
    name: str
    category: str
    price: float

class AddProductModel(BaseModel):
    name: str
    category: str
    price: float
    vendor_id: str

class AddInventoryModel(BaseModel):
    product_id: str
    vendor_id: str
    quantity: int
    expiry_date: date

class InventoryModel(BaseModel):
    batch_id: uuid.UUID
    p_id: uuid.UUID
    product_name: str
    product_category: str
    vendor_id: str
    quantity: int
    is_discounted: bool
    discount_percentage: float
    expiry_date: date

class ExpiryData(BaseModel):
    batch_id: uuid.UUID
    product_id: uuid.UUID
    product_name: str
    days_remaining: int
    date_added: date
    
class DiscountData(BaseModel):
    batch_id: uuid.UUID
    is_discounted: bool
    discount_percentage: float

class PredictData(BaseModel):
    product_name: str
    product_id: str
    