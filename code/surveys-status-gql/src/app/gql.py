from typing import Optional

import strawberry
import uvicorn
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter


@strawberry.type
class User:
    name: str
    age: int


async def query_users(name: Optional[str] = "") -> list[User]:
    users = [
        User(name="Patrick", age=100),
        User(name="Jorge", age=13),
        User(name="Fátima", age=56),
    ]
    if name:
        result = [u for u in users if name and u.name == name]
    else:
        result = users
    return result


@strawberry.type
class Query:
    users: list[User] = strawberry.field(resolver=query_users)


schema = strawberry.Schema(query=Query)

graphql_router = GraphQLRouter(schema)

app = FastAPI()

app.include_router(graphql_router, prefix="/graphql")

if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", reload=True)
