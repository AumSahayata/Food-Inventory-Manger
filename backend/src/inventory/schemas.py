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
    product_name: str
    product_category: str
    vendor_id: str
    quantity: int
    expiry_date: date