from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from service.handlers.exceptions import ResponseHeaders

router = APIRouter()


class Health(BaseModel):
    message: str = "API is running"


@router.get("/health")
def get_health() -> Health:
    return JSONResponse(
        content=jsonable_encoder(Health(), by_alias=True),
        headers=ResponseHeaders.JSON_HEADERS.value,
        status_code=status.HTTP_200_OK,
    )
