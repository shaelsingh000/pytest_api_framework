import pytest

@pytest.mark.skip(reason="jsonplaceholder does not persist posts")
def test_create_and_fetch_post(session,base_url):
    payload = {"title": "chain test", "body": "using response in next call", "userId": 1}
    response = session.post(f"{base_url}/posts", json=payload)
    assert response.status_code == 201
    post_data = response.json()
    post_id = post_data["id"]

    request_get = session.get(f"{base_url}/posts/{post_id}")
    assert request_get.status_code == 200