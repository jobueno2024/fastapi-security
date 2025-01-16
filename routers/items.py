from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Item(BaseModel):
    name: str
    price: float

@router.get("/")
async def read_items():
    return [{"name": "Item1", "price": 50.2}, {"name": "Item2", "price": 30.5}]

@router.post("/")
async def create_item(item: Item):
    return {"item": item, "message": "Item created successfully"}
