from sqlmodel import Field, SQLModel, Column
from datetime import datetime
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

class Inventory(SQLModel, table=True):
    batch_id: uuid.UUID = Field(
        sa_column = Column(
            pg.UUID,
            nullable = False,
            primary_key = True,
            default = uuid.uuid4
        )
    )
    product_id: uuid.UUID = Field(foreign_key="products.p_id", default=None)
    quantity: int
    expiry_date: datetime
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
