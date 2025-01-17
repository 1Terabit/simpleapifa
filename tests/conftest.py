import pytest
import uuid
from fastapi.testclient import TestClient
from app.main import app
from app.database import SessionLocal
from app.models import User, Item, Comment

@pytest.fixture(scope="module")
def test_client():
    client = TestClient(app)
    yield client

@pytest.fixture(scope="function")
def setup_database():
    db = SessionLocal()
    
    # Limpiar la base de datos antes de cada prueba
    # db.query(Comment).delete()
    # db.query(Item).delete()
    # db.query(User).delete()
    # db.commit()
    
    #NOTE: Crear un usuario con un nombre y un email únicos
    unique_username = f"testuser-{uuid.uuid4()}"
    unique_email = f"{unique_username}@example.com"
    user = User(username=unique_username, email=unique_email, password="securepassword")
    
    #NOTE: Crear un ítem
    unique_item_name = f"Test Item {uuid.uuid4()}"
    item = Item(name=unique_item_name, description="This is a test item.")
    
    db.add(user)
    db.add(item)
    
    #NOTE: Confirmar los cambios
    db.commit()
    
    yield {
        "user_id": user.id,
        "item_id": item.id
    }
