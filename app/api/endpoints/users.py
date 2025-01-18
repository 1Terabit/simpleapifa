from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models import User
from app.schemas import UserCreate, UserResponse
from app.database import get_db
from app.exceptions import NotFoundException
from app.services.user_service import create_user, get_users, delete_user, update_user

router = APIRouter()

@router.post("/", response_model=UserResponse, summary="Crear un nuevo usuario")
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    """
    Crea un nuevo usuario.

    - **username**: Nombre de usuario del nuevo usuario.
    - **email**: Correo electrónico del nuevo usuario.
    - **password**: Contraseña del nuevo usuario.
    """
    return create_user(db=db, user=user)

@router.get("/", response_model=list[UserResponse], summary="Obtener todos los usuarios")
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Obtiene una lista de usuarios.

    - **skip**: Número de usuarios a omitir (por defecto 0).
    - **limit**: Número máximo de usuarios a devolver (por defecto 10).
    """
    return get_users(db=db, skip=skip, limit=limit)

@router.get("/{user_id}", response_model=UserResponse, summary="Obtener un usuario por ID")
def read_user(user_id: int, db: Session = Depends(get_db)):
    """
    Obtiene un usuario por su ID.

    - **user_id**: ID del usuario a obtener.
    """
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise NotFoundException(detail="User not found")
    return user

@router.put("/{user_id}", response_model=UserResponse, summary="Actualizar un usuario")
def update_user_endpoint(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    """
    Actualiza un usuario existente.

    - **user_id**: ID del usuario a actualizar.
    - **username**: Nuevo nombre de usuario.
    - **email**: Nuevo correo electrónico.
    - **password**: Nueva contraseña.
    """
    updated_user = update_user(db=db, user_id=user_id, user=user)
    if updated_user is None:
        raise NotFoundException(detail="User not found")
    return updated_user

@router.delete("/{user_id}", response_model=UserResponse, summary="Delete User")
def delete_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    """
    Elimina un usuario por su ID.

    - **user_id**: ID del usuario a eliminar.
    """
    user = delete_user(db=db, user_id=user_id)
    if user is None:
        raise NotFoundException(detail="User not found")
    return user 