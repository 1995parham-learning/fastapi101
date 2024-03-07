import pydantic


class User(pydantic.BaseModel):
    first_name: str
    last_name: str
    age: int
