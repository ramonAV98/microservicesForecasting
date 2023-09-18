from fastapi.testclient import TestClient

from .app import webapp

client = TestClient(webapp.fastapi)


def test_app():
    response = client.get("/info")
    data = response.json()
    assert data == {"app_name": "anyForecast"}
