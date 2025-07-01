from datetime import datetime
from typing import Optional

import strawberry
from pydantic import BaseModel


class SurveysStatusModel(BaseModel):
    loaded_at: datetime
    status: str
    count: int


@strawberry.type
class Status:
    aberto: Optional[int] = None
    pendente: Optional[int] = None
    valido: Optional[int] = None
    invalido: Optional[int] = None
    visualizou: Optional[int] = None
    incompleto: Optional[int] = None


@strawberry.type
class SurveysStatus:
    date: datetime
    total: int
    status: Status
