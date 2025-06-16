from fastapi.testclient import TestClient
import pytest
from app.api import app


@pytest.fixture
def client():
    yield TestClient(app)


@pytest.fixture
def surveys_status_filter():
    return {
        "createdAt": {
            "start": "2025-01-01T00:19:30.899Z",
            "end": "2025-12-31T23:19:30.899Z",
        },
        "limit": 100,
        "offset": 10,
    }
