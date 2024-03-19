"""
Users related APIs are implemented here as function.
"""

import datetime
import typing
import uuid

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
    average: float = pydantic.Field(ge=0)
    graduation_date: datetime.date | None = pydantic.Field(default=None)

    @pydantic.field_validator("first_name", "last_name")
    @classmethod
    def check_alphanumeric(cls, v: str, info: pydantic.ValidationInfo) -> str:
        """
        check first name and last to be alphanumeric.
        """
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
        id=uuid.uuid4().hex,
        first_name=user.first_name,
        last_name=user.last_name,
        registration_date=datetime.date.today(),
        average=user.average,
        graduation_date=user.graduation_date,
    )
    storage.append(user_)

    return user_
