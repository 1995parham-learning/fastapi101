"""
End-to-end testings for APIs.
"""

from unittest import TestCase

from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, StaticPool, create_engine

from .db import get_db
from .main import app

SQLALCHEMY_DATABASE_URL = "sqlite://"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)


SQLModel.metadata.create_all(engine)


def override_get_db():
    db = Session(autocommit=False, autoflush=False, bind=engine)
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


class TestMain(TestCase):
    """
    test all the endpoints using the main application.
    """

    client = TestClient(app)

    def test_user_delete_not_found(self):
        """
        Delete a user which doesn't exists.
        """
        response = self.client.delete(f"/users/not-found")
        assert response.status_code == 404

    def test_user_retrieve_not_found(self):
        """
        Retrieve a user which doesn't exists.
        """
        response = self.client.get(f"/users/not-found")
        assert response.status_code == 404

    def test_user_create_and_delete(self):
        """
        Create a user and then delete it.
        """
        future_user = {
            "first_name": "Parham",
            "last_name": "Alvani",
            "average": 18.0,
        }

        response = self.client.post(
            "/users",
            json=future_user,
        )
        assert response.status_code == 200
        user = response.json()
        for key, value in future_user.items():
            assert user[key] == value

        response = self.client.get(f"/users/{user['id']}")
        assert response.status_code == 200

        response = self.client.delete(f"/users/{user['id']}")
        assert response.status_code == 200

    def test_users_create_and_list(self):
        """
        Create valid users and make sure it returns in the users list.
        """

        future_users = [
            {
                "first_name": "Parham",
                "last_name": "Alvani",
                "average": 18.0,
            },
            {
                "first_name": "Elahe",
                "last_name": "Dastan",
                "average": 20.0,
            },
            {
                "first_name": "Seyed Parham",
                "last_name": "Alvani",
                "average": 18.5,
            },
        ]

        for user in future_users:
            response = self.client.post(
                "/users",
                json=user,
            )
            assert response.status_code == 200
            assert user.items() <= response.json().items()

        response = self.client.get("/users")
        assert response.status_code == 200
        users = response.json()
        assert len(users) == len(future_users)

    def test_users_bad_create(self):
        """
        Create a invalid user and make sure it returns error.
        """

        for user in [
            {
                "first_name": "Parham1",
                "last_name": "Alvani",
                "average": 18,
            },
            {
                "first_name": "Parham",
                "last_name": "Alvani",
                "average": -1,
            },
        ]:
            response = self.client.post(
                "/users",
                json=user,
            )
            assert response.status_code == 422
