"""
End-to-end testings for APIs.
"""

from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_users_create_and_list():
    """
    Create valid users and make sure it returns in the users list.
    """

    future_users = [
        {
            "first_name": "Parham",
            "last_name": "Alvani",
            "age": 30,
        },
        {
            "first_name": "Elahe",
            "last_name": "Dastan",
            "age": 20,
        },
        {
            "first_name": "Seyed Parham",
            "last_name": "Alvani",
            "age": 30,
        },
    ]

    for user in future_users:
        response = client.post(
            "/users",
            json=user,
        )
        assert response.status_code == 200
        assert response.json() == user

    response = client.get("/users")
    assert response.status_code == 200
    users = response.json()
    assert len(users) == len(future_users)
    assert users == future_users


def test_users_bad_create():
    """
    Create a invalid user and make sure it returns error.
    """

    for user in [
        {
            "first_name": "Parham1",
            "last_name": "Alvani",
            "age": 30,
        },
        {
            "first_name": "Parham",
            "last_name": "Alvani",
            "age": -30,
        },
    ]:
        response = client.post(
            "/users",
            json=user,
        )
        assert response.status_code == 422
