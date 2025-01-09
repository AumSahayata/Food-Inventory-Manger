from sqlmodel import Field, SQLModel, Column
from datetime import date
import sqlalchemy.dialects.postgresql as pg
import uuid

class Products(SQLModel, table=True):
    __tablename__ = "products"
    p_id: uuid.UUID = Field(
        sa_column = Column(
            pg.UUID,
            nullable = False,
            primary_key = True,
            default = uuid.uuid4
        )
    )
    name: str
    category: str
    price: float
    vendor_id: str

class Inventory(SQLModel, table=True):
    __tablename__ = "inventory"
    batch_id: uuid.UUID = Field(
        sa_column = Column(
            pg.UUID,
            nullable = False,
            primary_key = True,
            default = uuid.uuid4
        )
    )
    product_id: uuid.UUID = Field(foreign_key="products.p_id", default=None)
    vendor_id: str
    quantity: int
    expiry_date: date
    created_at: date = Field(sa_column=Column(pg.TIMESTAMP, default=date.today()))
    
class Sales(SQLModel, table=True):
    __tablename__ = "sales"
    
    sale_id:uuid.UUID = Field(
        sa_column = Column(
            pg.UUID,
            nullable = False,
            primary_key = True,
            default = uuid.uuid4
        )
    )
    product_id: uuid.UUID = Field(foreign_key="products.p_id", default=None)
    sale_date: date
    is_holiday: bool
    sale_day: int
    quantity_sold: int

class Expiry(SQLModel, table=True):
    