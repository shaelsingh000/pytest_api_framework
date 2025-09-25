import pytest
import requests

def test_invalid_endpoint(session,base_url):
    response = session.get(f"{base_url}/invalid_endpoint")
    assert response.status_code == 404
def test_invalid_post_payload(session, base_url):
    payload = {"wrong_field": "data"}  # missing required fields
    response = session.post(f"{base_url}/posts", json=payload)
    # jsonplaceholder returns 201 anyway, in real API expect 400
    assert response.status_code in [201, 400]  
def test_unauthorized_access():
    url = "https://httpbin.org/basic-auth/user/pass"
    response = requests.get(url, auth=("user", "wrongpass"))
    assert response.status_code == 401

@pytest.mark.parametrize(
    "endpoint, expected_status",
    [
        ("/invalid_endpoint", 404),
        ("/posts/999999", 404)
    ]
)
def test_parametrized_negative(session, base_url, endpoint, expected_status):
    response = session.get(f"{base_url}{endpoint}")
    assert response.status_code == expected_status
