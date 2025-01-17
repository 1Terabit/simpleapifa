import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_user(test_client, setup_database):
    response = client.post("/users/", json={
        "username": "testuser",
        "email": "testuser@example.com",
        "password": "securepassword"
    })
    assert response.status_code == 200
    assert response.json()["username"].startswith("testuser")

def test_read_user(test_client, setup_database):
    response = client.get(f"/users/{setup_database['user_id']}")
    assert response.status_code == 200
    assert response.json()["username"].startswith("testuser")

def test_delete_user(test_client, setup_database):
    response = client.delete(f"/users/{setup_database['user_id']}")
    assert response.status_code == 200
    assert response.json()["username"].startswith("testuser") 