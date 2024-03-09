"""
Users related APIs are implemented here as function.
"""

import typing

import fastapi

from app import domain, services

router = fastapi.APIRouter()


@router.get("/", tags=["users"])
async def users_list(
    storage: typing.Annotated[services.Storage, fastapi.Depends()]
) -> list[domain.User]:
    """
    List currently stored users.
    """
    storage.append(domain.User(first_name="Elahe", last_name="Dastan", age=24))

    return storage.all()
