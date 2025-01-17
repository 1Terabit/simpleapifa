import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_comment(test_client, setup_database):
    response = client.post("/comments/", json={
        "item_id": setup_database["item_id"],
        "user_id": setup_database["user_id"],
        "content": "This is a test comment."
    })
    assert response.status_code == 200
    assert response.json()["content"] == "This is a test comment."

def test_read_comment(test_client, setup_database):
    #NOTE: Primero, crea un comentario para asegurarte de que existe
    create_response = client.post("/comments/", json={
        "item_id": setup_database["item_id"],
        "user_id": setup_database["user_id"],
        "content": "This is a test comment."
    })
    comment_id = create_response.json()["id"]  #NOTE: Obtener el ID del comentario creado
    response = client.get(f"/comments/{comment_id}")  #NOTE: Usar el ID del comentario creado
    assert response.status_code == 200
    assert response.json()["content"] == "This is a test comment."

def test_delete_comment(test_client, setup_database):
    #NOTE: Primero, crea un comentario para asegurarte de que existe
    create_response = client.post("/comments/", json={
        "item_id": setup_database["item_id"],
        "user_id": setup_database["user_id"],
        "content": "This is a test comment."
    })
    comment_id = create_response.json()["id"]  #NOTE: Obtener el ID del comentario creado
    response = client.delete(f"/comments/{comment_id}")  #NOTE: Usar el ID del comentario creado
    assert response.status_code == 200
    assert response.json()["content"] == "This is a test comment." 