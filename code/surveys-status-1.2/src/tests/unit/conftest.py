from fastapi.testclient import TestClient
import pytest
from app.api import app


@pytest.fixture
def client():
    yield TestClient(app)
