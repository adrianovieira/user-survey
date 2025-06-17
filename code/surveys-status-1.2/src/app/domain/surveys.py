from models.surveys import Status, SurveysStatusRequest, SurveysStatusResponse

from adapter.repositories.surveys import SurveysRepository
from domain.commands.surveys import SurveysStatusCommand


def get_surveys(filter_with: SurveysStatusRequest):

    surveys_repository = SurveysRepository()
    surveys_data: list[SurveysStatusCommand] = (
        surveys_repository.get_surveys_by_loaded_at(filter_with)
    )

    surveys_data_dto: list[SurveysStatusResponse] = []
    if surveys_data:
        date_left = surveys_data[0].loaded_at
        status: Status = {}
        total_date = 0
        for sd in surveys_data:
            date_right = sd.loaded_at
            if date_left != date_right:
                surveys_data_dto.append(
                    SurveysStatusResponse(
                        date=date_left,
                        total=total_date,
                        status=status,
                    )
                )

                status = {}
                if sd.count:
                    status[sd.status] = sd.count
                total_date = sd.count
            else:
                if sd.count:
                    status[sd.status] = sd.count
                total_date += sd.count

            date_left = date_right

    return surveys_data_dto
