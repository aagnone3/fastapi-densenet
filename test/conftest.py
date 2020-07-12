import pytest

from starlette.testclient import TestClient

from app.main import app

@pytest.fixture(scope='function')
def api_client() -> TestClient:
    return TestClient(app)
