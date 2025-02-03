# from typing import Annotated

# from fastapi import Depends
# from fastapi.security import HTTPBasic, HTTPBasicCredentials
# from fastapi import APIRouter

# router = APIRouter()
# security = HTTPBasic()


# @router.post("")
# def read_current_user(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
#     return {"username": credentials.username, "password": credentials.password}

from fastapi import Depends, FastAPI
from fastapi.security import APIKeyHeader
from fastapi import APIRouter

router = APIRouter()

header_scheme = APIKeyHeader(name="x-key")


@router.get("")
async def read_items(key: str = Depends(header_scheme)):
    return {"key": key}