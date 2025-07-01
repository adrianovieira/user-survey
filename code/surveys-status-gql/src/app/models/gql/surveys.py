from datetime import datetime
from typing import NewType, Optional

from pydantic import BaseModel
from strawberry import scalar as strawberry_scalar
from strawberry import type as strawberry_type

# TODO: testar integração de strawberry e pydantic


class SurveysStatusModel(BaseModel):
    loaded_at: datetime
    status: str
    count: int


TGqlJSON = strawberry_scalar(
    NewType("TGqlJSON", object),
    description="The `JSON` scalar type represents JSON values as specified by ECMA-404",
    serialize=lambda s: s,
    parse_value=lambda v: v,
)


@strawberry_type
class Status:
    aberto: Optional[int] = None
    pendente: Optional[int] = None
    valido: Optional[int] = None
    invalido: Optional[int] = None
    visualizou: Optional[int] = None
    incompleto: Optional[int] = None


@strawberry_type
class SurveysStatus:
    date: datetime
    total: int
    status: TGqlJSON
