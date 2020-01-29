from http import HTTPStatus

from flaskblueprint.models import db, User


def test_get_users(client):
    data = {"username": "test", "password": "123"}
    response = client.post("/auth/login", json=data)

    assert "token" in response.get_json()
    token = response.get_json()["token"]
    auth_header = {"Authorization": f"Bearer {token}"}

    user = User(username="test2", password="test2")
    db.session.add(user)
    db.session.commit()

    response = client.get("/users/all", headers=auth_header)

    assert response.status_code == HTTPStatus.OK, "Get all users fail"
    assert len(response.get_json()) == 2

    response = client.get(f"/users/{user.id}", headers=auth_header)

    assert response.status_code == HTTPStatus.OK, "Get one user fail"
    assert response.get_json()["id"] == str(user.id)
    assert response.get_json()["username"] == user.username


def test_create_user_fail(client):
    data = {"username": "test", "password": "123"}
    response = client.post("/auth/login", json=data)

    assert "token" in response.get_json()
    token = response.get_json()["token"]
    auth_header = {"Authorization": f"Bearer {token}"}

    user_data = {}
    response = client.post("/users/", json=user_data, headers=auth_header)

    assert response.status_code == HTTPStatus.BAD_REQUEST, "Create User fail"
    data = response.get_json()
    assert data["message"] == "No input data provided"

    user_data = {"invalid_field": ""}
    response = client.post("/users/", json=user_data, headers=auth_header)

    assert response.status_code == HTTPStatus.BAD_REQUEST, "Create User fail"
    data = response.get_json()["error"]
    assert data["username"] == ["Missing data for required field."]
    assert data["invalid_field"] == ["Unknown field."]
