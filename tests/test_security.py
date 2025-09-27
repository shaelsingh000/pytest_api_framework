import pytest
import requests

BASE_URL = "https://api.github.com/user"

def test_unauthorized_get(session):
    # Assuming /users endpoint requires auth
    response = session.get(f"{BASE_URL}/users")
    # Should fail because no auth provided
    assert response.status_code in [401, 403]

def test_invalid_token(session):
    headers = {"Authorization": "Bearer invalid_token_123"}
    response = session.get(f"{BASE_URL}/users", headers=headers)
    assert response.status_code in [401, 403]

def test_sql_injection(session):
    payload = {"name": "' OR 1=1 --", "job": "hacker"}
    response = session.post(f"{BASE_URL}/users", json=payload)
    # API should not accept malicious input
    assert response.status_code != 500  # Should not crash
