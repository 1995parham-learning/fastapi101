import datetime

import pydantic


class User(pydantic.BaseModel):
    """
    The user model to handle user in the application.
    """

    id: str
    first_name: str
    last_name: str
    registration_date: datetime.date
