from app.controllers.gql.surveys_query import query_surveys_status
from app.controllers.gql.users_query import query_users
from app.models.gql.surveys import SurveysStatus
from app.models.gql.users import User
from strawberry import Schema
from strawberry import field as strawberry_field
from strawberry import type as strawberry_type


@strawberry_type
class Query:
    users: list[User] = strawberry_field(resolver=query_users)
    surveysStatus: list[SurveysStatus] = strawberry_field(resolver=query_surveys_status)


query_schema = Schema(query=Query)
