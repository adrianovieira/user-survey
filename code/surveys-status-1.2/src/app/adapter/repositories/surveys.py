from datetime import datetime
from service.uow.sqlalchemy import SqlAlchemyUnitOfWork
from sqlalchemy import select
from adapter.orm.surveys import MVSurveysStatus
from domain.commands.surveys import SurveysStatusCommand
from models.surveys import SurveysStatusRequest


class SurveysRepository:
    uow: SqlAlchemyUnitOfWork

    def __init__(self, uow: SqlAlchemyUnitOfWork = SqlAlchemyUnitOfWork()):
        self.uow: SqlAlchemyUnitOfWork = uow

    def get_surveys(self, filter_with: SurveysStatusRequest = {}):

        sql = select(MVSurveysStatus)
        if filter_with:
            if "createdAt" in filter_with and filter_with["createdAt"]["start"]:
                sql = sql.where(
                    MVSurveysStatus.loaded_at
                    >= datetime.fromisoformat(filter_with["createdAt"]["start"])
                )
            if "createdAt" in filter_with and filter_with["createdAt"]["end"]:
                sql = sql.where(
                    MVSurveysStatus.loaded_at
                    <= datetime.fromisoformat(filter_with["createdAt"]["end"])
                )

            if "limit" in filter_with and filter_with["limit"]:
                sql = sql.limit(int(filter_with["limit"]))
            if "offset" in filter_with and filter_with["offset"]:
                sql = sql.offset(int(filter_with["offset"]))

        with self.uow as db:
            result = db.execute(sql).all()

        surveys_data: list[SurveysStatusCommand]
        if result:
            surveys_data = [
                SurveysStatusCommand.model_validate(res[0], from_attributes=True)
                for res in result
            ]
        return surveys_data
