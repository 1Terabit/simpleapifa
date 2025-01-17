import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.models import Item

client = TestClient(app)

def test_create_item(test_client, setup_database):
    response = client.post("/items/", json={
        "name": "Test Item",
        "description": "This is a test item."
    })
    assert response.status_code == 200
    assert response.json()["name"].startswith("Test Item")  

def test_read_item(test_client, setup_database):
    response = client.get(f"/items/{setup_database['item_id']}")
    assert response.status_code == 200
    assert response.json()["name"].startswith("Test Item")  

def test_delete_item(test_client, setup_database):
    response = client.delete(f"/items/{setup_database['item_id']}")
    assert response.status_code == 200
    assert response.json()["name"].startswith("Test Item")  
