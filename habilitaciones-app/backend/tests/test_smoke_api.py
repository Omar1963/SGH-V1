from fastapi.testclient import TestClient

from app.main import app


def test_root_healthcheck():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json().get("message") == "SGH-V1 API is running"


def test_openapi_available():
    client = TestClient(app)
    response = client.get("/api/v1/openapi.json")
    assert response.status_code == 200
    assert response.json().get("openapi")
