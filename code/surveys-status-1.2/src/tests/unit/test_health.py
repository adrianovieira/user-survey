class TestMonitoramentos:

    def test_health(self, client):
        response = client.get("health")

        assert response.status_code == 200
        content = response.json()
        assert content == {"message": "API is running"}
        assert content["message"] == "API is running"
