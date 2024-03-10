"""
Storages for users.
"""

from app import domain


class Storage:
    """
    In memory storage for users.
    """

    storage: list[domain.User] = []

    def __init__(self):
        pass

    def append(self, user: domain.User):
        self.storage.append(user)

    def all(self) -> list[domain.User]:
        return self.storage
