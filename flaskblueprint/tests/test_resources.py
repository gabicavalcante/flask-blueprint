from http import HTTPStatus

from flaskblueprint.models import db, Task


def test_get_tasks(client):
    data = {"username": "test", "password": "123"}
    response = client.post("/auth/login", json=data)

    assert "token" in response.get_json()
    token = response.get_json()["token"]
    auth_header = {"Authorization": f"Bearer {token}"}

    response = client.get("/tasks/all", headers=auth_header)

    assert response.status_code == HTTPStatus.OK, "Get all tasks fail"
    assert response.get_json() == []

    task = Task(description="description", script="test")
    db.session.add(task)
    db.session.commit()

    response = client.get("/tasks/all", headers=auth_header)

    assert response.status_code == HTTPStatus.OK, "Get all tasks fail"
    assert response.get_json()[0]["description"] == task.description

    response = client.get(f"/tasks/{task.id}", headers=auth_header)

    assert response.status_code == HTTPStatus.OK, "Get one task fail"


def test_create_task_fail(client):
    data = {"username": "test", "password": "123"}
    response = client.post("/auth/login", json=data)

    assert "token" in response.get_json()
    token = response.get_json()["token"]
    auth_header = {"Authorization": f"Bearer {token}"}

    task_data = {}
    response = client.post("/tasks/", json=task_data, headers=auth_header)

    assert response.status_code == HTTPStatus.BAD_REQUEST, "Create Task fail"
    data = response.get_json()
    assert data["message"] == "No input data provided"

    task_data = {"invalid_field": ""}
    response = client.post("/tasks/", json=task_data, headers=auth_header)

    assert response.status_code == HTTPStatus.BAD_REQUEST, "Create Task fail"
    data = response.get_json()["error"]
    assert data["description"] == ["Missing data for required field."]
    assert data["invalid_field"] == ["Unknown field."]
