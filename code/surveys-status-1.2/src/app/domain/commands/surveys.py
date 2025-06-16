from datetime import datetime

from pydantic import BaseModel


class SurveysStatusCommand(BaseModel):
    loaded_at: datetime
    status: str
    count: int
