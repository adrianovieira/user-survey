from service.uow.sqlalchemy import SqlAlchemyUnitOfWork
from sqlalchemy import select
from adapter.orm.surveys import MVSurveysStatus
from domain.commands.surveys import SurveysStatusCommand


class SurveysRepository:
    uow: SqlAlchemyUnitOfWork

    def __init__(self, uow: SqlAlchemyUnitOfWork = SqlAlchemyUnitOfWork()):
        self.uow: SqlAlchemyUnitOfWork = uow

    def get_surveys(self, filter_attributes: dict = {}):
        sql = select(MVSurveysStatus)
        with self.uow as db:
            result = db.execute(sql).all()

        surveys_data: list[SurveysStatusCommand]
        if result:
            surveys_data = [
                SurveysStatusCommand.model_validate(res[0], from_attributes=True)
                for res in result
            ]
        return surveys_data
