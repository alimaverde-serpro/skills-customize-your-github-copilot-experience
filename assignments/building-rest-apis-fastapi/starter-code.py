from typing import Dict, Optional

from fastapi import FastAPI, HTTPException, Query, status
from pydantic import BaseModel, Field

app = FastAPI(title="FastAPI REST Assignment")


class ItemCreate(BaseModel):
    name: str = Field(min_length=1)
    price: float = Field(gt=0)
    description: Optional[str] = None


class ItemUpdate(BaseModel):
    name: Optional[str] = Field(default=None, min_length=1)
    price: Optional[float] = Field(default=None, gt=0)
    description: Optional[str] = None


class Item(ItemCreate):
    id: int


items_db: Dict[int, Item] = {}
next_id = 1


@app.get("/")
def root() -> dict:
    return {"message": "Welcome to your FastAPI assignment"}


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/items", response_model=Item, status_code=status.HTTP_201_CREATED)
def create_item(payload: ItemCreate) -> Item:
    global next_id

    new_item = Item(id=next_id, **payload.model_dump())
    items_db[next_id] = new_item
    next_id += 1
    return new_item


@app.get("/items", response_model=list[Item])
def list_items(name: Optional[str] = Query(default=None)) -> list[Item]:
    all_items = list(items_db.values())
    if name is None:
        return all_items

    lowered = name.lower()
    return [item for item in all_items if lowered in item.name.lower()]


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int) -> Item:
    item = items_db.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, payload: ItemUpdate) -> Item:
    existing = items_db.get(item_id)
    if existing is None:
        raise HTTPException(status_code=404, detail="Item not found")

    updated_data = existing.model_dump()
    patch_data = payload.model_dump(exclude_unset=True)
    updated_data.update(patch_data)
    updated_item = Item(**updated_data)
    items_db[item_id] = updated_item
    return updated_item


@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int) -> None:
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")

    del items_db[item_id]
    return None
