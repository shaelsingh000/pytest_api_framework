def test_get_post(session, base_url):
    response = session.get(f"{base_url}/posts/1")
    data = response.json()
    assert response.status_code == 200
    assert "title" in data
    assert "body" in data

def test_create_post(session, base_url):
    payload = {"title":"foo","body":"bar","userId": 1}
    response = session.post(f"{base_url}/posts", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "foo"

    