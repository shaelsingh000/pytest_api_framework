import requests
from jsonschema import validate

user_schema = {
    "type": "object",
    "properties": {
        "userId": {"type": "integer"},
        "id": {"type": "integer"},
        "title": {"type": "string"},
        "body": {"type": "string"}
    },
    "required": ["userId", "id", "title", "body"]
}


def test_post_schema_validation(session, base_url):
    response = session.get(f"{base_url}/posts/1")
    assert response.status_code == 200
    validate(instance=response.json(), schema=user_schema)