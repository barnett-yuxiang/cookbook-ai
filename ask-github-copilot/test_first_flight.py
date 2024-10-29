import pytest
from fastapi.testclient import TestClient
from first_flight import app

# test_first_flight.py


client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_read_item():
    item_id = 1
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    assert response.json() == {"item_id": item_id, "q": None}


def test_read_item_with_query():
    item_id = 1
    query = "test_query"
    response = client.get(f"/items/{item_id}?q={query}")
    assert response.status_code == 200
    assert response.json() == {"item_id": item_id, "q": query}
