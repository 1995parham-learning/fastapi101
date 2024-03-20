"""
the user model definition.
"""

import datetime

import sqlmodel


class User(sqlmodel.SQLModel, table=True):
    """
    The user model to handle user in the application.
    """

    id: str = sqlmodel.Field(primary_key=True)
    first_name: str
    last_name: str
    registration_date: datetime.date
    graduation_date: datetime.date | None = None
    average: float
