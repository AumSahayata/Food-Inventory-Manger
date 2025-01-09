from fastapi import FastAPI
from src.inventory.routes import inventory_router

app = FastAPI()

app.include_router(inventory_router, prefix="api/inv")