import responses
import requests

BASE_URL = "https://api.example.com"

@responses.activate
def test_mock_get_user():
    # Mock the GET endpoint
    responses.add(
        responses.GET,
        f"{BASE_URL}/user/1",
        json={"id": 1, "name": "John Doe"},
        status=200
    )

    response = requests.get(f"{BASE_URL}/user/1")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "John Doe"

@responses.activate
def test_mock_post_user_error():
    # Mock POST endpoint returning 500
    responses.add(
        responses.POST,
        f"{BASE_URL}/user",
        json={"error": "Internal Server Error"},
        status=500
    )

    payload = {"name": "Alice"}
    response = requests.post(f"{BASE_URL}/user", json=payload)
    assert response.status_code == 500
    assert response.json()["error"] == "Internal Server Error"
