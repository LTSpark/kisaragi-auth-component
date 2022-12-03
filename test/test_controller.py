from fastapi.testclient import TestClient

from main import app
from app.internal import DatabaseConfig

DatabaseConfig().connect_database()

client = TestClient(app)


# USER CONTROLLER
def test_create_user():
    response = client.post(
        "/api/v1/users",
        json={
            "user_name": "Edward Ramos",
            "email": "edward.ramos30@gmail.com",
            "password": "Edward123",
            "birth_date": "2022-11-12",
            "telephone_number": "123456789",
            "role": "ADMIN"
        }
    )
    assert response.status_code == 201
    assert "user" in response.json()


def test_create_user_fail():
    response = client.post(
        "/api/v1/users",
        json={
            "hola": "adios"
        }
    )
    assert response.status_code == 422


def test_update_user_fail():
    user_id = '636f5a05d9cfa8310661c40c'
    files=dict(foo='bar')
    
    response = client.put(
        f"/api/v1/users/{user_id}",
        json={
            "user_id": "636f5a05d9cfa8310661c40c",
            "name": "Arian Z.",
            "file":files
        }, files=dict(foo='bar')
    )
    assert response.status_code == 422


def test_get_user_by_email():
    email = "arian30@gmail.com"
    response = client.get(
        f"/api/v1/users/{email}/email"
    )
    assert response.status_code == 200
    assert "user_id" in response.json()


def test_get_user_by_email_fail():
    email = ""
    response = client.get(
        f"/api/v1/users/{email}/email"
    )
    assert response.status_code == 404


def test_get_user_by_id():
    user_id = '636f5a05d9cfa8310661c40c'
    
    response = client.get(
        f"/api/v1/users/{user_id}/id"
    )
    assert response.status_code == 200
    assert "user_id" in response.json()


# HEALTH CONTROLLER
def test_create_user_health():
    response = client.get(
        "/api/v1/health"
    )
    assert response.json() == {"msg": "Everything is OK!", "status": "Healthy"}


# AUTHENTICATION CONTROLLER
def test_login_user():
    response = client.post(
        "/api/v1/auth",
        json={
            'email': "arian30@gmail.com",
            'password': "Arian123"
        }
    )
    assert response.status_code == 200
    assert "user" in response.json()


def test_login_user_fail1():
    response = client.post(
        "/api/v1/auth",
        json={
            'email': "arian29@gmail.com",
            'password': "Arian123"
        }
    )
    assert response.status_code == 404


def test_login_user_fail2():
    response = client.post(
        "/api/v1/auth"
    )
    assert response.status_code == 422
