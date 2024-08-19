from fastapi.testclient import TestClient
from server import app
import requests

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}

def test_name():
    name = "Arthur"
    response = client.get(f"/{name}")
    assert response.status_code == 200
    assert response.json() == {"message": f"Hello {name}!"}

def test_api_cat_fact(monkeypatch):
    def mock_get(url):
        class MockResponse:
            def json(self):
                return [{"text": "Cats sleep 70% of their lives."}]
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)
    
    response = client.get("/api/cat-fact")
    assert response.status_code == 200
    assert response.json() == "Cats sleep 70% of their lives."
