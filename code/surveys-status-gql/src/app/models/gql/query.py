import strawberry
from app.controllers.gql.users_query import query_users
from app.models.gql.users import User


@strawberry.type
class Query:
    users: list[User] = strawberry.field(resolver=query_users)


query_schema = strawberry.Schema(query=Query)
