from datetime import datetime

import strawberry
from pydantic import BaseModel


class SurveysStatusModel(BaseModel):
    loaded_at: datetime
    status: str
    count: int


@strawberry.type
class Status:
    aberto: int | None = None
    pendente: int | None = None
    valido: int | None = None
    invalido: int | None = None
    visualizou: int | None = None
    incompleto: int | None = None


@strawberry.type
class SurveysStatus:
    date: datetime
    total: int
    status: Status
