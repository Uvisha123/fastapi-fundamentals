from pydantic import BaseModel
from typing import Optional

class ItemCreate(BaseModel):
    name: str
    price: float
    description: Optional[str] = None

class ItemOut(BaseModel):
    id: int
    name: str
    price: float
