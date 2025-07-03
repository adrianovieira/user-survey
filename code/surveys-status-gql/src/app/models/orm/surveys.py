from datetime import datetime

from sqlalchemy import BigInteger, DateTime, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column

from .base import ORMBase


class UsersSurveysResponseAux(ORMBase):
    __tablename__ = "users_surveys_responses_aux"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    origin: Mapped[str] = mapped_column(String(15))
    response_status_id: Mapped[int] = mapped_column(Integer)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )


class MVSurveysStatus(ORMBase):
    __tablename__ = "mv_survey_loaded_at_status"

    loaded_at: Mapped[datetime] = mapped_column(primary_key=True)
    status: Mapped[str] = mapped_column(String(15), primary_key=True)
    count: Mapped[int] = mapped_column(Integer)
