import uvicorn
from app.routes.gql.users_route import graphql_router
from fastapi import FastAPI

app = FastAPI()

app.include_router(graphql_router, prefix="/graphql")

if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", reload=True)
