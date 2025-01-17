from sqlalchemy.orm import Session
from ..models.user import User
from ..schemas.user import UserCreate

def create_user(db: Session, user: UserCreate):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user 

def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first() 

def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
        return user
    return None 

def update_user(db: Session, user_id: int, user: UserCreate):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db_user.username = user.username
        db_user.email = user.email
        db_user.password = user.password  #NOTE Asegúrate de manejar la contraseña de forma segura
        db.commit()
        db.refresh(db_user)
        return db_user
    return None 