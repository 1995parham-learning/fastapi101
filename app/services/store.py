"""
Storages for users.
"""

import fastapi
import sqlmodel

from app import db, domain


class DuplicateEntry(Exception):
    """
    Duplicate user identification.
    """

    def __init__(self, user_id: str):
        self.user_id = user_id

        super().__init__()

    def __str__(self):
        return f"duplicate user ({self.user_id})"


class Storage:
    """
    Database storage for users.
    """

    def __init__(self, session: sqlmodel.Session = fastapi.Depends(db.get_db)):
        self.session = session

    def append(self, user: domain.User):
        """
        Register new user.
        """
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)

    def retrieve(self, user_id: str) -> domain.User | None:
        """
        Retrieve the user by ID.
        """
        stmt = sqlmodel.select(domain.User).where(domain.User.id == user_id)

        return self.session.exec(stmt).first()

    def delete(self, user_id: str) -> domain.User | None:
        """
        Delete the user by ID.
        """
        stmt = sqlmodel.select(domain.User).where(domain.User.id == user_id)

        user = self.session.exec(stmt).first()

        if user is None:
            return None

        self.session.delete(user)
        self.session.commit()

        return user

    def all(self) -> list[domain.User]:
        """
        Return all the registered users.
        """
        stmt = sqlmodel.select(domain.User)

        return list(self.session.exec(stmt))
