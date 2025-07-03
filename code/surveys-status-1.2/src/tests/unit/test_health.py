from fastapi import Response
from fastapi.testclient import TestClient


class TestMonitoramentos:

    def test_health(self, client):
        response = client.get("health")

        assert response.status_code == 200
        content = response.json()
        assert content == {"message": "API is running"}
        assert content["message"] == "API is running"

    def test_cors_enabled(self, client: TestClient):
        headers = {
            "Origin": "http://localhost:3000",
            "Accept": "application/json",
            "Content-Type": "application/json; charset=utf-8",
        }
        response: Response = client.get("/health", headers=headers)
        assert response.status_code == 200

        # print(response.headers)
        assert "cache-control" in response.headers
        assert response.headers["cache-control"] == "no-store"
        assert "x-content-type-options" in response.headers
        assert response.headers["x-content-type-options"] == "nosniff"

        assert "access-control-allow-origin" in response.headers
        assert (
            response.headers["access-control-allow-origin"] == "http://localhost:3000"
        )
