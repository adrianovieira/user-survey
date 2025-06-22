class TestSurveys:

    def test_surveys_status(self, client):
        response = client.post("/surveys/status")

        assert response.status_code == 200
        content = response.json()
        content_one: dict = content[0]

        assert "date" in content_one.keys()
        assert "total" in content_one.keys()
        assert "status" in content_one.keys()
        assert any(content_one["status"].values())

    def test_surveys_status_filter(self, client, surveys_status_filter: dict):

        response = client.post("/surveys/status", json=surveys_status_filter)
        assert response.status_code == 200
        content = response.json()
        content_one: dict = content[0]
        assert "date" in content_one.keys()
        assert "total" in content_one.keys()
        assert "status" in content_one.keys()
        assert any(content_one["status"].values())

        surveys_status_filter.pop("offset")
        response = client.post("/surveys/status", json=surveys_status_filter)
        assert response.status_code == 200
        content = response.json()
        content_one: dict = content[0]
        assert "date" in content_one.keys()
        assert "total" in content_one.keys()
        assert "status" in content_one.keys()
        assert any(content_one["status"].values())

        surveys_status_filter.pop("limit")
        response = client.post("/surveys/status", json=surveys_status_filter)
        assert response.status_code == 200
        content = response.json()
        content_one: dict = content[0]
        assert "date" in content_one.keys()
        assert "total" in content_one.keys()
        assert "status" in content_one.keys()
        assert any(content_one["status"].values())

        surveys_status_filter["createdAt"].pop("start")
        response = client.post("/surveys/status", json=surveys_status_filter)
        assert response.status_code == 200
        content = response.json()
        content_one: dict = content[0]
        assert "date" in content_one.keys()
        assert "total" in content_one.keys()
        assert "status" in content_one.keys()
        assert any(content_one["status"].values())

        surveys_status_filter["createdAt"].pop("end")
        response = client.post("/surveys/status", json=surveys_status_filter)

        assert response.status_code == 200
        content = response.json()
        content_one: dict = content[0]
        assert "date" in content_one.keys()
        assert "total" in content_one.keys()
        assert "status" in content_one.keys()
        assert any(content_one["status"].values())

    def test_surveys_status_filter_no_data(self, client, surveys_status_filter: dict):
        surveys_status_filter["createdAt"] = {"start": "2100-06-14T18:19:30.899Z"}
        response = client.post("/surveys/status", json=surveys_status_filter)

        assert response.status_code == 200
        content = response.json()
        assert content == []

    def test_surveys_status_errors(self, client, surveys_status_filter: dict):
        surveys_status_filter["createdAt"] = {"start": "06-14-2005T18:19:30.899Z"}
        response = client.post("/surveys/status", json=surveys_status_filter)

        assert response.status_code == 400
        content = response.json()
        print(content)
        assert content == {
            "namespace": "service.handlers.exceptions",
            "informationLink": "http://api.isurvey.localhost",
            "code": "VL001",
            "name": "VALIDATION_ERROR",
            "message": "Incorrectly reported attributes.",
            "correlationId": None,
            "debugId": None,
            "details": [
                {
                    "field": "createdAt->start",
                    "issue": "Input should be a valid datetime or date, invalid character in year",
                    "location": "body",
                }
            ],
        }
