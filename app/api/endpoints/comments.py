from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models import Comment
from app.schemas import CommentCreate, CommentResponse
from app.database import get_db
from app.exceptions import NotFoundException
from app.services.comment_service import create_comment, get_comments, delete_comment, update_comment

router = APIRouter()

@router.post("/", response_model=CommentResponse, summary="Crear un nuevo comentario")
def create_comment_endpoint(comment: CommentCreate, db: Session = Depends(get_db)):
    """
    Crea un nuevo comentario.

    - **item_id**: ID del ítem al que se asocia el comentario.
    - **user_id**: ID del usuario que realiza el comentario.
    - **content**: Contenido del comentario.
    """
    return create_comment(db=db, comment=comment)

@router.get("/", response_model=list[CommentResponse], summary="Obtener todos los comentarios")
def read_comments(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Obtiene una lista de comentarios.

    - **skip**: Número de comentarios a omitir (por defecto 0).
    - **limit**: Número máximo de comentarios a devolver (por defecto 10).
    """
    return get_comments(db=db, skip=skip, limit=limit)

@router.get("/{comment_id}", response_model=CommentResponse, summary="Obtener un comentario por ID")
def read_comment(comment_id: int, db: Session = Depends(get_db)):
    """
    Obtiene un comentario por su ID.

    - **comment_id**: ID del comentario a obtener.
    """
    comment = db.query(Comment).filter(Comment.id == comment_id).first()
    if comment is None:
        raise NotFoundException(detail="Comment not found")
    return comment

@router.put("/{comment_id}", response_model=CommentResponse, summary="Actualizar un comentario")
def update_comment_endpoint(comment_id: int, comment: CommentCreate, db: Session = Depends(get_db)):
    """
    Actualiza un comentario existente.

    - **comment_id**: ID del comentario a actualizar.
    - **content**: Nuevo contenido del comentario.
    """
    updated_comment = update_comment(db=db, comment_id=comment_id, comment=comment)
    if updated_comment is None:
        raise NotFoundException(detail="Comment not found")
    return updated_comment

@router.delete("/{comment_id}", response_model=CommentResponse, summary="Eliminar un comentario")
def delete_comment_endpoint(comment_id: int, db: Session = Depends(get_db)):
    """
    Elimina un comentario por su ID.

    - **comment_id**: ID del comentario a eliminar.
    """
    comment = delete_comment(db=db, comment_id=comment_id)
    if comment is None:
        raise NotFoundException(detail="Comment not found")
    return comment 