from datetime import datetime

from adapter.orm.surveys import MVSurveysStatus
from domain.commands.surveys import SurveysStatusCommand
from models.surveys import SurveysStatusRequest
from service.handlers.exceptions import APIExceptionInfo
from service.uow.sqlalchemy import SqlAlchemyUnitOfWork
from sqlalchemy import select


class SurveysRepository:
    uow: SqlAlchemyUnitOfWork

    def __init__(self, uow: SqlAlchemyUnitOfWork = SqlAlchemyUnitOfWork()):
        self.uow: SqlAlchemyUnitOfWork = uow

    def get_surveys_by_loaded_at(self, filter_with: SurveysStatusRequest = {}):
        sql = select(MVSurveysStatus).order_by(MVSurveysStatus.loaded_at)
        where = ""

        if filter_with:
            if (
                "createdAt" in filter_with
                and filter_with["createdAt"]
                and filter_with["createdAt"]["start"]
            ):
                sql = sql.where(
                    MVSurveysStatus.loaded_at
                    >= datetime.fromisoformat(filter_with["createdAt"]["start"])
                )
                where = "WHERE loaded_at >= '" + filter_with["createdAt"]["start"] + "'"

            if (
                "createdAt" in filter_with
                and filter_with["createdAt"]
                and filter_with["createdAt"]["end"]
            ):
                sql = sql.where(
                    MVSurveysStatus.loaded_at
                    <= datetime.fromisoformat(filter_with["createdAt"]["end"])
                )
                if where:
                    where += " AND "
                else:
                    where = "where "

            if "limit" in filter_with and filter_with["limit"]:
                sql = sql.limit(int(filter_with["limit"]))
            if "offset" in filter_with and filter_with["offset"]:
                sql = sql.offset(int(filter_with["offset"]))

        with self.uow as db:
            result = db.execute(sql).fetchall()

        if not result:
            raise APIExceptionInfo(status_code=404)

        surveys_data: list[SurveysStatusCommand] = [
            SurveysStatusCommand.model_validate(res[0], from_attributes=True)
            for res in result
        ]

        return surveys_data
