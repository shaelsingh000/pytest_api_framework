import pytest 
def authenticate_basic(username,password):
    if username=="user" and password == "pass":
        return {"authenticated": True, "user": username}, 200
    return {"authenticated": False, "user": username}, 401
def test_basic_auth_success():
    data,status_code = authenticate_basic("user","pass")
    assert status_code == 200
    assert data["authenticated"] is True
def test_basic_auth_failure():
    data,status_code = authenticate_basic("user","password")
    assert status_code == 401
    assert data["authenticated"] is False