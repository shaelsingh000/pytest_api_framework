import pytest
import requests
import json
import csv
import os

BASE_URL = "https://reqres.in/api"

def load_json_data():
    file_path = os.path.join(os.path.dirname(__file__), "..", "data", "users.json")
    with open(file_path, "r") as f:
        return json.load(f)
    
def load_csv_data():
    file_path = os.path.join(os.path.dirname(__file__), "..", "data", "users.csv")
    with open(file_path, "r") as f:
        reader = csv.DictReader(f)
        return [row for row in reader]
    
@pytest.mark.parametrize("user",load_json_data())
def test_create_user_from_json(session,user):
    response = session.post(f"{BASE_URL}/users",json=user)
    assert response.status_code == 201
    res_body = response.json()
    print("Response Status:", response.status_code)
    print("Response Body:", response.text)
    assert res_body["name"] == user["name"]
    assert res_body["job"] == user["job"]

@pytest.mark.parametrize("user", load_csv_data())
def test_create_user_from_csv(session, user):
    response = session.post(f"{BASE_URL}/users", json=user)
    assert response.status_code == 201
    res_body = response.json()
    print("Response Status:", response.status_code)
    print("Response Body:", response.text)
    assert res_body["name"] == user["name"]
    assert res_body["job"] == user["job"]