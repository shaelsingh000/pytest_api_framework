import pytest

@pytest.mark.parametrize(
    "post_id, expected_user",
    [
        (1, 1),
        (2, 1),
        (3, 1),
        (10, 1)
    ]
)

def test_get_posts_parametrized(session,base_url,post_id,expected_user):
    response = session.get(f"{base_url}/posts/{post_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["userId"]==expected_user