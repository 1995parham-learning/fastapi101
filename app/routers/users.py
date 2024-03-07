import typing

import fastapi

from app import domain, services

router = fastapi.APIRouter()


@router.get("/", tags=["users"])
async def list(
    storage: typing.Annotated[services.Storage, fastapi.Depends()]
) -> list[domain.User]:
    storage.append(domain.User(first_name="Elahe", last_name="Dastan", age=24))

    return storage.all()
