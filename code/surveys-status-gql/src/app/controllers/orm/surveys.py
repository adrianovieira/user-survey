from app.models.gql.surveys import SurveysStatusModel
from app.models.orm.surveys import MVSurveysStatus
from app.service.uow.sqlalchemy import SqlAlchemyUnitOfWork
from sqlalchemy import select


def fetch_db_all_survey_status(orm: SqlAlchemyUnitOfWork = SqlAlchemyUnitOfWork()):
    sql = select(MVSurveysStatus).order_by(MVSurveysStatus.loaded_at)

    # TODO: adicionar recurso de filtro where / limit / offset

    with orm as db:
        result = db.execute(sql).fetchall()

    surveys_data: list[SurveysStatusModel] = [
        SurveysStatusModel.model_validate(res[0], from_attributes=True)
        for res in result
    ]

    return surveys_data
