import pytest
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# ----------------------------
# Basic GET response time test
# ----------------------------
def test_get_post_response_time(session, base_url, max_response_time):
    response = session.get(f"{base_url}/posts/1")
    elapsed = response.elapsed.total_seconds()
    logger.info(f"GET /posts/1 response time: {elapsed:.3f}s, status: {response.status_code}")

    assert response.status_code == 200
    assert elapsed <= max_response_time

# ---------------------------------------
# Parametrized response time for multiple endpoints
# ---------------------------------------
@pytest.mark.parametrize(
    "endpoint",
    ["/posts/1", "/comments/1", "/albums/1"]
)
def test_multiple_endpoints_response_time(session, base_url, endpoint, max_response_time):
    response = session.get(f"{base_url}{endpoint}")
    elapsed = response.elapsed.total_seconds()
    logger.info(f"GET {endpoint} response time: {elapsed:.3f}s, status: {response.status_code}")

    assert response.status_code == 200
    assert elapsed <= max_response_time

# ----------------------------
# Test with fixture for max response time
# ----------------------------
def test_response_time_with_fixture(session, base_url, max_response_time):
    response = session.get(f"{base_url}/posts/1")
    elapsed = response.elapsed.total_seconds()
    logger.info(f"GET /posts/1 response time: {elapsed:.3f}s, status: {response.status_code}")

    assert response.status_code == 200
    assert elapsed <= max_response_time
