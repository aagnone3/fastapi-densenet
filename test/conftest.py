import pytest

from starlette.testclient import TestClient

from fastapi_sentiment.main import app

@pytest.fixture(scope='function')
def api_client() -> TestClient:
    return TestClient(app)
