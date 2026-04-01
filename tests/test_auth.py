from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register_endpoint():
    response = client.post(
        "/api/auth/register",
            json={"username": "newuser", "password": "secretpassword"}
    )

    assert response.status_code in [201,400]