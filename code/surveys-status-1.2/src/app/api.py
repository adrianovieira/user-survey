import uvicorn
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from pydantic import ValidationError
from routes import health, surveys
from service.handlers.exceptions import APIException, api_exception_handler

app = FastAPI()

app.add_exception_handler(APIException, api_exception_handler)
app.add_exception_handler(ValidationError, api_exception_handler)
app.add_exception_handler(RequestValidationError, api_exception_handler)

app.include_router(health.router)
app.include_router(surveys.router)

if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", reload=True)
