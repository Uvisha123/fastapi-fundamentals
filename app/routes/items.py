from fastapi import APIRouter
from app.schemas.item import ItemCreate
from fastapi import HTTPException

router = APIRouter()

@router.get("/items/{item_id}")
def get_item(item_id: int):
    return {
        "item_id": item_id,
        "message": "Item fetched successfully"
    }

@router.get("/items")
def get_items(skip: int = 0, limit: int = 10):
    return {
        "skip": skip,
        "limit": limit,
        "items": []
    }

@router.post("/items")
def create_item(item: ItemCreate):
    return {"item_created": item}


@router.put("/items/{item_id}")
def update_item(item_id: int, item: ItemCreate):
    return {
        "item_id": item_id,
        "updated_item": item
    }
    
@router.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {
        "item_id": item_id,
        "status": "deleted"
    }
    