from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_add_and_get_active_prompt():
    res = client.post("/prompts", json={"text": "Give short, polite answers."})
    assert res.status_code == 200
    assert res.json()["version"] == 2

    active = client.get("/prompts/active")
    assert active.json()["text"] == "Give short, polite answers."