from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine
from .models.user import User
from .models.item import Item
from .models.comment import Comment
from .api.endpoints import users, items, comments
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from app.exceptions import NotFoundException, BadRequestException

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

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=400,
        content={"detail": exc.errors(), "body": exc.body},
    )

@app.exception_handler(NotFoundException)
async def not_found_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )

@app.exception_handler(BadRequestException)
async def bad_request_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    ) 