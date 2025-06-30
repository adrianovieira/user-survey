import logging
from enum import Enum
from uuid import uuid4

from fastapi import Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, ValidationError

logger = logging.getLogger()


class APIMessageError(str, Enum):
    UNEXPECTED_ERROR = "Unexpected error."
    VALIDATION_ERROR = "Incorrectly reported attributes."
    REQUEST_ERROR = "Invalid request content."
    NOT_FOUND = "Surveys data not found."


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
    debug_id: str | None = Field(default=str(uuid4()), alias="debugId")
    details: list[APIErrorDetails] | None = []


class APIInternalServerErrorResponse(APIErrorResponse):
    name: str = "INTERNAL_SERVER_ERROR"
    code: str = "IE001"
    message: str = APIMessageError.UNEXPECTED_ERROR


class APIServiceUnavailableErrorResponse(APIErrorResponse):
    name: str = "SERVICE_UNAVAILABLE_ERROR"
    code: str = "IE002"
    message: str = APIMessageError.UNEXPECTED_ERROR


class APIValidationErrorResponse(APIErrorResponse):
    name: str = "VALIDATION_ERROR"
    code: str = "VE001"
    message: str = APIMessageError.VALIDATION_ERROR
    details: list[APIErrorDetails] | None = None


class APIRequestValidationErrorResponse(APIErrorResponse):
    name: str = "VALIDATION_ERROR"
    code: str = "VE002"
    message: str = APIMessageError.REQUEST_ERROR


class APIDataNotFoundResponse(APIErrorResponse):
    name: str = "NOT_FOUND"
    code: str = "NF001"
    message: str = APIMessageError.NOT_FOUND


API_ERRORS_RESPONSES = {
    status.HTTP_400_BAD_REQUEST: APIRequestValidationErrorResponse,
    status.HTTP_404_NOT_FOUND: APIDataNotFoundResponse,
    status.HTTP_422_UNPROCESSABLE_ENTITY: APIValidationErrorResponse,
    status.HTTP_500_INTERNAL_SERVER_ERROR: APIInternalServerErrorResponse,
    status.HTTP_503_SERVICE_UNAVAILABLE: APIServiceUnavailableErrorResponse,
}


class APIException(Exception):

    def __init__(
        self,
        status_code: int,
        message: str | None = None,
        code: str | None = None,
        details: RequestValidationError | ValidationError | None = None,
    ):
        self.status_code = status_code
        self.api_error = API_ERRORS_RESPONSES.get(status_code)
        self.error_response: APIErrorResponse = self.api_error()


class APIExceptionError(APIException): ...


class APIExceptionWarning(APIException): ...


class APIExceptionInfo(APIException): ...


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
    request: Request,
    exception: APIException | ValidationError | RequestValidationError,
):
    if isinstance(exception, ValidationError) or isinstance(
        exception, RequestValidationError
    ):
        errors = exception.errors()

        details = [
            APIErrorDetails(
                field=(
                    "->".join(error["loc"][1:])
                    if len(error["loc"][1:]) > 1
                    else str(error["loc"][0])
                ),
                issue=(
                    error["ctx"]["error"] if hasattr(error, "ctx") else error["msg"]
                ),
                location=str(error["loc"][0]),
            )
            for error in errors
        ]

        if isinstance(exception, ValidationError):
            status_code = 400
            error_response = APIValidationErrorResponse(
                status_code=status_code, details=details
            )
        else:
            status_code = 422
            error_response = APIRequestValidationErrorResponse(
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
