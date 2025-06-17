from datetime import datetime
from service.uow.sqlalchemy import SqlAlchemyUnitOfWork
from sqlalchemy import select, text
from adapter.orm.surveys import MVSurveysStatus
from domain.commands.surveys import SurveysStatusCommand
from models.surveys import SurveysStatusRequest


class SurveysRepository:
    uow: SqlAlchemyUnitOfWork

    def __init__(self, uow: SqlAlchemyUnitOfWork = SqlAlchemyUnitOfWork()):
        self.uow: SqlAlchemyUnitOfWork = uow

    def get_surveys_by_loaded_at(self, filter_with: SurveysStatusRequest = {}):
        sql = select(MVSurveysStatus).order_by(MVSurveysStatus.loaded_at)
        limit = ""
        offset = ""
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
                where += "loaded_at <= '" + filter_with["createdAt"]["end"] + "'"

            if "limit" in filter_with and filter_with["limit"]:
                sql = sql.limit(int(filter_with["limit"]))
                limit = "LIMIT " + str(filter_with["limit"])
            if "offset" in filter_with and filter_with["offset"]:
                sql = sql.offset(int(filter_with["offset"]))
                offset = "OFFSET " + str(filter_with["offset"])

        sql_text = text(
            f"select * from inside.mv_survey_loaded_at_status {where} order by loaded_at {limit} {offset}"
        )

        with self.uow as db:
            # # a busca via orm retorna dados errados :O
            # # sob análise a solução definitiva
            # result = db.execute(sql).fetchall()

            # # solução de contorno
            result = db.execute(sql_text).fetchall()

        surveys_data: list[SurveysStatusCommand] = []
        if result:
            surveys_data = [
                SurveysStatusCommand.model_validate(res, from_attributes=True)
                for res in result
            ]
        return surveys_data
