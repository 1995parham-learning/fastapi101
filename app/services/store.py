"""
Storages for users.
"""

from app import domain


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
    In memory storage for users.
    """

    storage: dict[str, domain.User] = {}

    def __init__(self):
        pass

    def append(self, user: domain.User):
        """
        Register new user.
        """
        if user.id not in self.storage:
            self.storage[user.id] = user

    def retrieve(self, user_id: str) -> domain.User | None:
        """
        Retrieve the user by ID.
        """
        return self.storage.get(user_id, None)

    def delete(self, user_id: str) -> domain.User | None:
        """
        Delete the user by ID.
        """
        user = self.storage.get(user_id, None)
        if user is None:
            return None
        del self.storage[user_id]
        return user

    def all(self) -> list[domain.User]:
        """
        Return all the registered users.
        """
        return list(self.storage.values())
