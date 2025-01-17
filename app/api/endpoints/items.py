from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..dependencies import get_db
from ...schemas.item import ItemCreate, ItemResponse
from ...services.item_service import create_item, get_items, delete_item, update_item

router = APIRouter()

@router.post("/", response_model=ItemResponse, summary="Crear un nuevo ítem", 
             description="Este endpoint permite crear un nuevo ítem en la base de datos.")
def create_item_endpoint(item: ItemCreate, db: Session = Depends(get_db)):
    """
    Crea un nuevo ítem.

    - **name**: Nombre del ítem.
    - **description**: Descripción del ítem.
    """
    return create_item(db=db, item=item)

@router.get("/", response_model=list[ItemResponse], summary="Obtener todos los ítems", 
             description="Este endpoint permite obtener una lista de todos los ítems.")
def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Obtiene una lista de ítems.

    - **skip**: Número de ítems a omitir (por defecto 0).
    - **limit**: Número máximo de ítems a devolver (por defecto 10).
    """
    return get_items(db=db, skip=skip, limit=limit)

@router.delete("/{item_id}", response_model=ItemResponse, summary="Eliminar un ítem", 
             description="Este endpoint permite eliminar un ítem existente por su ID.")
def delete_item_endpoint(item_id: int, db: Session = Depends(get_db)):
    """
    Elimina un ítem por su ID.

    - **item_id**: ID del ítem a eliminar.
    """
    item = delete_item(db=db, item_id=item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.put("/{item_id}", response_model=ItemResponse, summary="Actualizar un ítem", 
             description="Este endpoint permite actualizar un ítem existente por su ID.")
def update_item_endpoint(item_id: int, item: ItemCreate, db: Session = Depends(get_db)):
    """
    Actualiza un ítem existente.

    - **item_id**: ID del ítem a actualizar.
    - **name**: Nuevo nombre del ítem.
    - **description**: Nueva descripción del ítem.
    """
    updated_item = update_item(db=db, item_id=item_id, item=item)
    if updated_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated_item 