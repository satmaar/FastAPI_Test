from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_root_returns_welcome_message() -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Hello, FastAPI"}


def test_greet_returns_name_in_message() -> None:
    response = client.get("/greet/Ada")

    assert response.status_code == 200
    assert response.json() == {"message": "Hello, Ada!"}


def test_docs_and_openapi_are_available() -> None:
    docs_response = client.get("/docs")
    openapi_response = client.get("/openapi.json")

    assert docs_response.status_code == 200
    assert "Swagger UI" in docs_response.text
    assert openapi_response.status_code == 200
    assert "/greet/{name}" in openapi_response.json()["paths"]
