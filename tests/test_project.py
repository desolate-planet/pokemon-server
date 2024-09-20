from flask import json


def test_fetch_pokemon(client):
    response = client.get("/pokemon/api/v1")
    assert response.status_code == 200
    data = json.loads(response.text)
    assert len(data) == 50


