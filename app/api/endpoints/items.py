from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..dependencies import get_db
from ...schemas.item import ItemCreate, ItemResponse
from ...services.item_service import create_item, get_items, delete_item, update_item

router = APIRouter()

@router.post("/", response_model=ItemResponse)
def create_item_endpoint(item: ItemCreate, db: Session = Depends(get_db)):
    return create_item(db=db, item=item)

@router.get("/", response_model=list[ItemResponse])
def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_items(db=db, skip=skip, limit=limit)

@router.delete("/{item_id}", response_model=ItemResponse)
def delete_item_endpoint(item_id: int, db: Session = Depends(get_db)):
    item = delete_item(db=db, item_id=item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.put("/{item_id}", response_model=ItemResponse)
def update_item_endpoint(item_id: int, item: ItemCreate, db: Session = Depends(get_db)):
    updated_item = update_item(db=db, item_id=item_id, item=item)
    if updated_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated_item 