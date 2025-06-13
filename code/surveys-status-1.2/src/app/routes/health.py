from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter()


class Health(BaseModel):
    message: str = "API is running"


@router.get("/health")
def get_health() -> Health:
    return {"message": "API is running"}
