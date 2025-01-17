from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..dependencies import get_db
from ...schemas.comment import CommentCreate, CommentResponse
from ...services.comment_service import create_comment, get_comment_by_id, delete_comment, update_comment

router = APIRouter()

@router.post("/", response_model=CommentResponse, summary="Crear un nuevo comentario", 
             description="Este endpoint permite crear un nuevo comentario en la base de datos.")
def create_comment_endpoint(comment: CommentCreate, db: Session = Depends(get_db)):
    """
    Crea un nuevo comentario.

    - **item_id**: ID del ítem al que se asocia el comentario.
    - **user_id**: ID del usuario que realiza el comentario.
    - **content**: Contenido del comentario.
    """
    return create_comment(db=db, comment=comment)

@router.get("/{comment_id}", response_model=CommentResponse, summary="Obtener un comentario por ID", 
             description="Este endpoint permite obtener un comentario existente por su ID.")
def read_comment(comment_id: int, db: Session = Depends(get_db)):
    """
    Obtiene un comentario por su ID.

    - **comment_id**: ID del comentario a obtener.
    """
    comment = get_comment_by_id(db=db, comment_id=comment_id)
    if comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return comment

@router.delete("/{comment_id}", response_model=CommentResponse, summary="Eliminar un comentario", 
             description="Este endpoint permite eliminar un comentario existente por su ID.")
def delete_comment_endpoint(comment_id: int, db: Session = Depends(get_db)):
    """
    Elimina un comentario por su ID.

    - **comment_id**: ID del comentario a eliminar.
    """
    comment = delete_comment(db=db, comment_id=comment_id)
    if comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return comment

@router.put("/{comment_id}", response_model=CommentResponse, summary="Actualizar un comentario", 
             description="Este endpoint permite actualizar un comentario existente por su ID.")
def update_comment_endpoint(comment_id: int, comment: CommentCreate, db: Session = Depends(get_db)):
    """
    Actualiza un comentario existente.

    - **comment_id**: ID del comentario a actualizar.
    - **item_id**: Nuevo ID del ítem asociado.
    - **user_id**: Nuevo ID del usuario que realiza el comentario.
    - **content**: Nuevo contenido del comentario.
    """
    updated_comment = update_comment(db=db, comment_id=comment_id, comment=comment)
    if updated_comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return updated_comment 