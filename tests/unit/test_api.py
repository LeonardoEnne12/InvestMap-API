from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "online"
    print("[OK] test_root_endpoint passed")


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert "status" in data
    assert "database" in data
    print("[OK] test_health_endpoint passed")


if __name__ == "__main__":
    print("Running API Unit Tests...")
    test_root_endpoint()
    test_health_endpoint()
    print("API Unit Tests Completed Successfully!")
