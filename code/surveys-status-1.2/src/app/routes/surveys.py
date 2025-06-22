from domain.surveys import get_surveys
from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from models.surveys import SurveysStatusRequest, SurveysStatusResponse

router = APIRouter()


@router.post(
    "/surveys/status",
)
def post_surveys_status(
    req: SurveysStatusRequest | None = None,
) -> list[SurveysStatusResponse]:
    request = jsonable_encoder(req)
    result = get_surveys(request)
    return jsonable_encoder(result)
