"""
Users related APIs are implemented here as function.
"""

import typing

import fastapi
import pydantic

from app import domain, services

router = fastapi.APIRouter()


class User(pydantic.BaseModel):
    """
    User creation request.
    """

    first_name: str = pydantic.Field()
    last_name: str = pydantic.Field()
    age: int = pydantic.Field(
        gt=0,
    )

    @pydantic.field_validator("first_name", "last_name")
    @classmethod
    def check_alphanumeric(cls, v: str, info: pydantic.ValidationInfo) -> str:
        assert isinstance(v, str), f"{info.field_name} must be string"

        is_alphanumeric = v.replace(" ", "").isalpha()
        # info.field_name is the name of the field being validated
        assert is_alphanumeric, f"{info.field_name} must be alphabetic"

        return v


@router.get("/", tags=["users"])
async def users_list(
    storage: typing.Annotated[services.Storage, fastapi.Depends()]
) -> list[domain.User]:
    """
    List currently stored users.
    """
    return storage.all()


@router.post("/", tags=["users"])
async def users_new(
    storage: typing.Annotated[services.Storage, fastapi.Depends()],
    user: User,
):
    """
    Create another user from the request.
    """
    user_ = domain.User(
        first_name=user.first_name,
        last_name=user.last_name,
        age=user.age,
    )
    storage.append(user_)

    return user_
