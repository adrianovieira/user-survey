from app.controllers.orm.surveys import fetch_db_all_survey_status
from app.models.gql.surveys import Status, SurveysStatus, SurveysStatusModel


async def query_surveys_status() -> list[SurveysStatus]:
    surveys_data: SurveysStatusModel = fetch_db_all_survey_status()

    # TODO: criar cache em Redis

    surveys_data_dto: list[SurveysStatus] = []
    if surveys_data:
        date_left = surveys_data[0].loaded_at
        status: Status = {}
        total_date = 0
        for sd in surveys_data:
            date_right = sd.loaded_at
            if date_left != date_right:
                surveys_data_dto.append(
                    SurveysStatus(
                        date=date_left,
                        total=total_date,
                        status=status,
                    )
                )

                status = {}
                if sd.count:
                    status[sd.status.lower()] = sd.count
                total_date = sd.count
            else:
                if sd.count:
                    status[sd.status.lower()] = sd.count
                total_date += sd.count

            date_left = date_right

    return surveys_data_dto
