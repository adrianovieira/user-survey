from enum import Enum
import logging
from fastapi import Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel, ConfigDict, Field, ValidationError

logger = logging.getLogger()


class APIMessageError(str, Enum):
    UNEXPECTED_ERROR = "Unexpected error."
    VALIDATION_ERROR = "Incorrectly reported attributes."


class APIErrorDetails(BaseModel):
    field: str
    issue: str
    location: str


class APIErrorResponse(BaseModel):
    namespace: str = Field(default=__name__)
    information_link: str = Field(
        default="http://api.isurvey.localhost", alias="informationLink"
    )
    code: str
    name: str
    message: str | None = None
    correlation_id: str | None = Field(default=None, alias="correlationId")
    debug_id: str | None = Field(default=None, alias="debugId")
    details: APIErrorDetails | None = None


class APIInternalServerErrorResponse(APIErrorResponse):
    name: str = "INTERNAL_SERVER_ERROR"
    code: str = "IE001"
    message: str = APIMessageError.UNEXPECTED_ERROR


class APIServiceUnavailableErrorResponse(APIErrorResponse):
    name: str = "SERVICE_UNAVAILABLE_ERROR"
    code: str = "IE002"
    message: str = APIMessageError.UNEXPECTED_ERROR


class APIValidationErrorResponse(APIErrorResponse):
    model_config = ConfigDict(validate_assignment=True)
    name: str = "VALIDATION_ERROR"
    code: str = "VL001"
    message: str = APIMessageError.VALIDATION_ERROR
    details: list[APIErrorDetails] | None = None


class APIException(Exception):

    API_ERRORS = {
        status.HTTP_500_INTERNAL_SERVER_ERROR: APIInternalServerErrorResponse,
        status.HTTP_503_SERVICE_UNAVAILABLE: APIServiceUnavailableErrorResponse,
    }

    def __init__(
        self,
        status_code: int,
        message: str | None = None,
        code: str | None = None,
        details: RequestValidationError | ValidationError | None = None,
    ):
        self.status_code = status_code
        self.api_error = self.API_ERRORS.get(status_code)
        self.error_response: APIErrorResponse = self.api_error()


class APIExceptionError(APIException): ...


class APIExceptionWarning(APIException): ...


class ResponseHeaders(Enum):
    SECURITY_HEADERS = {
        "X-Content-Type-Options": "nosniff",
        "Cache-Control": "no-store",
    }
    JSON_HEADERS = {
        "Content-Type": "application/json; charset=utf-8",
        **SECURITY_HEADERS,
    }


async def api_exception_handler(
    request: Request, exception: APIException | ValidationError | RequestValidationError
):
    if isinstance(exception, ValidationError) or isinstance(
        exception, RequestValidationError
    ):
        print(type(exception))
        status_code = 400
        errors = exception.errors()
        details = [
            APIErrorDetails(
                field=(
                    "->".join(error["loc"][1:])
                    if len(error["loc"][1:]) >= 2
                    else str(error["loc"][1])
                ),
                issue=(
                    error["ctx"]["error"] if hasattr(error, "ctx") else error["msg"]
                ),
                location=str(error["loc"][0]),
            )
            for error in errors
        ]

        error_response = APIValidationErrorResponse(
            status_code=status_code, details=details
        )
    else:
        status_code = exception.status_code
        error_response = exception.error_response

    return JSONResponse(
        content=jsonable_encoder(error_response, by_alias=True),
        headers=ResponseHeaders.JSON_HEADERS.value,
        status_code=status_code,
    )
