import pytest
import requests
from config.settings import BASE_URL

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL

@pytest.fixture(scope="session")
def session():
    s=requests.Session()
    s.headers.update({"Content-Type" : "application/json"})
    yield s
    s.close()

@pytest.fixture
def max_response_time():
    return 2 # 500ms


