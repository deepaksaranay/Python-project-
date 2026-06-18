import pytest
from utils.api_client import APIClient

BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.fixture(scope="session")
def client():
    """Single APIClient instance for entire test session"""
    return APIClient(BASE_URL)

@pytest.fixture
def sample_post():
    """Sample payload for POST requests"""
    return {
        "title": "Test Post",
        "body": "Automated test content",
        "userId": 1
    }
