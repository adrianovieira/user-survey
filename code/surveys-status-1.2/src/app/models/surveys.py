from datetime import datetime
from pydantic import BaseModel, Field


class CreatedAt(BaseModel):
    start: datetime | None = None
    end: datetime | None = None


class SurveysStatusRequest(BaseModel):
    created_at: CreatedAt | None = Field(alias="createdAt", default=None)
    limit: int | None = Field(ge=0, default=None)
    offset: int | None = Field(ge=0, default=None)


class Status(BaseModel):
    aberto: int | None = Field(default=None, alias="Aberto")
    pendente: int | None = Field(default=None, alias="Pendente")
    valido: int | None = Field(default=None, alias="Válido")
    invalido: int | None = Field(default=None, alias="Inválido")
    visualizou: int | None = Field(default=None, alias="Visualizou")
    incompleto: int | None = Field(default=None, alias="Incompleto")


class SurveysStatusResponse(BaseModel):
    date: datetime
    total: int
    status: Status
