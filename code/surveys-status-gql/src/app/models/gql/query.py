import strawberry
from app.controllers.gql.surveys_query import query_surveys_status
from app.controllers.gql.users_query import query_users
from app.models.gql.surveys import SurveysStatus
from app.models.gql.users import User


@strawberry.type
class Query:
    users: list[User] = strawberry.field(resolver=query_users)
    surveysStatus: list[SurveysStatus] = strawberry.field(resolver=query_surveys_status)


query_schema = strawberry.Schema(query=Query)
