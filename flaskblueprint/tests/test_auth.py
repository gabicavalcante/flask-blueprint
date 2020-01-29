from http import HTTPStatus
from flaskblueprint.models import User, db
from flaskblueprint.ext.auth import verify_login


def test_login(client):
    data = {"username": "test", "password": "123"}
    response = client.post("/auth/login", json=data)

    assert "token" in response.get_json()

    token = response.get_json()["token"]
    response = client.get("/users/all", headers={"Authorization": f"Bearer {token}"})

    assert response.status_code == HTTPStatus.OK, "Create User fail"


def test_wrong_login(client):
    data = {"username": "error", "password": "error"}

    response = client.post("/auth/login", json=data)

    assert response.get_json() == {"message": "User error doesn't exist"}


def test_verify_login():
    user = User(username="teste", password="teste")
    db.session.add(user)
    db.session.commit()

    assert verify_login({"username": "teste", "password": "teste"})
    assert not verify_login({"username": "teste", "password": "error"})
    assert not verify_login({"username": "error", "password": "error"})
