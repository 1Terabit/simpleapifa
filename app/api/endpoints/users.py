from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..dependencies import get_db
from ...schemas.user import UserCreate, UserResponse
from ...services.user_service import create_user, get_user_by_id, delete_user, update_user

router = APIRouter()

@router.post("/", response_model=UserResponse, summary="Crear un nuevo usuario", 
             description="Este endpoint permite crear un nuevo usuario en la base de datos.")
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    """
    Crea un nuevo usuario.

    - **username**: Nombre de usuario del nuevo usuario.
    - **email**: Correo electrónico del nuevo usuario.
    - **password**: Contraseña del nuevo usuario.
    """
    return create_user(db=db, user=user)

@router.get("/{user_id}", response_model=UserResponse, summary="Obtener un usuario por ID", 
             description="Este endpoint permite obtener un usuario existente por su ID.")
def read_user(user_id: int, db: Session = Depends(get_db)):
    """
    Obtiene un usuario por su ID.

    - **user_id**: ID del usuario a obtener.
    """
    return get_user_by_id(db=db, user_id=user_id)

@router.delete("/{user_id}", response_model=UserResponse, summary="Eliminar un usuario", 
             description="Este endpoint permite eliminar un usuario existente por su ID.")
def delete_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    """
    Elimina un usuario por su ID.

    - **user_id**: ID del usuario a eliminar.
    """
    user = delete_user(db=db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}", response_model=UserResponse, summary="Actualizar un usuario", 
             description="Este endpoint permite actualizar un usuario existente por su ID.")
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
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user 