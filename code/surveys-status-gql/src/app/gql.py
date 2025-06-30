import uvicorn
from app.routes.gql.router import graphql_router
from app.service.handlers.exceptions import APIException, api_exception_handler
from fastapi import FastAPI
from fastapi.exceptions import ResponseValidationError
from pydantic import ValidationError

app = FastAPI()

# TODO: aprimorar tratamento de exeções
app.add_exception_handler(APIException, api_exception_handler)
app.add_exception_handler(ValidationError, api_exception_handler)
app.add_exception_handler(ResponseValidationError, api_exception_handler)

app.include_router(graphql_router, prefix="/graphql")

if __name__ == "__main__":
    uvicorn.run("gql:app", host="0.0.0.0", reload=True)
