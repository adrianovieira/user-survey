from models.surveys import Status, SurveysStatusRequest, SurveysStatusResponse

from adapter.repositories.surveys import SurveysRepository
from domain.commands.surveys import SurveysStatusCommand


def get_surveys(filter_with: SurveysStatusRequest):

    surveys_repository = SurveysRepository()
    surveys_data: list[SurveysStatusCommand] = surveys_repository.get_surveys(
        filter_with
    )

    date_left = surveys_data[0].loaded_at
    status: Status = {}
    surveys_data_dto: list[SurveysStatusResponse] = []
    total_date = 0
    for sd in surveys_data:
        date_right = sd.loaded_at
        if sd.count:
            status[sd.status] = sd.count
        total_date += sd.count
        if date_left != date_right:
            surveys_data_dto.append(
                SurveysStatusResponse(
                    date=date_left,
                    total=total_date,
                    status=status,
                )
            )
            status = {}
            total_date = 0

        date_left = date_right

    return surveys_data_dto
