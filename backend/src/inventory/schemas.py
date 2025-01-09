from pydantic import BaseModel

class ProductModel(BaseModel):
    name: str
    category: str
    price: float

class AddInventoryModel(BaseModel):
    