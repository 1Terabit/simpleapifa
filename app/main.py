from fastapi import FastAPI
from .database import engine
from .models.user import User
from .models.item import Item
from .models.comment import Comment
from .api.endpoints import users, items, comments

# Crear las tablas en la base de datos
User.metadata.create_all(bind=engine)
Item.metadata.create_all(bind=engine)
Comment.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(items.router, prefix="/items", tags=["items"])
app.include_router(comments.router, prefix="/comments", tags=["comments"]) 