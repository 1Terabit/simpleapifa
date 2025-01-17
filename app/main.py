from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine
from .models.user import User
from .models.item import Item
from .models.comment import Comment
from .api.endpoints import users, items, comments

#NOTE Crear las tablas en la base de datos
User.metadata.create_all(bind=engine)
Item.metadata.create_all(bind=engine)
Comment.metadata.create_all(bind=engine)

app = FastAPI()

#NOTE: Configurar CORS
origins = [
    "http://localhost:3000",  #NOTE: Reemplaza con el dominio de tu frontend
    "https://example.com",     #NOTE: Agrega otros dominios si es necesario
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  #NOTE: Permitir todos los métodos
    allow_headers=["*"],  #NOTE: Permitir todos los encabezados
)

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(items.router, prefix="/items", tags=["items"])
app.include_router(comments.router, prefix="/comments", tags=["comments"]) 