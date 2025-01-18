from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models import User
from app.schemas import UserCreate, UserResponse
from app.database import get_db
from app.exceptions import NotFoundException
from app.services.user_service import create_user, get_users, delete_user, update_user

router = APIRouter()

@router.post("/", response_model=UserResponse, summary="Create a new user")
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    """
    Creates a new user.

    - **username**: Username of the new user.
    - **email**: Email of the new user.
    - **password**: Password of the new user.
    """
    return create_user(db=db, user=user)

@router.get("/", response_model=list[UserResponse], summary="Get all users")
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Get a list of users.

    - **skip**: Number of users to skip (default 0).
    - **limit**: Maximum number of users to return (default 10).
    """
    return get_users(db=db, skip=skip, limit=limit)

@router.get("/{user_id}", response_model=UserResponse, summary="Get user by ID")
def read_user(user_id: int, db: Session = Depends(get_db)):
    """
    Get a user by ID.

    - **user_id**: ID of the user to retrieve.
    """
    user = get_user_by_id(db=db, user_id=user_id)
    if user is None:
        raise NotFoundException(detail="User not found")
    return user

@router.put("/{user_id}", response_model=UserResponse, summary="Update a user")
def update_user_endpoint(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    """
    Update an existing user.

    - **user_id**: ID of the user to update.
    - **username**: New username.
    - **email**: New email.
    - **password**: New password.
    """
    updated_user = update_user(db=db, user_id=user_id, user=user)
    if updated_user is None:
        raise NotFoundException(detail="User not found")
    return updated_user

@router.delete("/{user_id}", response_model=UserResponse, summary="Delete User")
def delete_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    """
    Delete a user by ID.

    - **user_id**: ID of the user to delete.
    """
    user = delete_user(db=db, user_id=user_id)
    if user is None:
        raise NotFoundException(detail="User not found")
    return user 