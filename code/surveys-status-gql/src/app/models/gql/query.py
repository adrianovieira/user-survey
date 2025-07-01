from app.controllers.gql.surveys_query import query_surveys_status
from app.models.gql.surveys import SurveysStatus
from strawberry import Schema
from strawberry import field as strawberry_field
from strawberry import type as strawberry_type


@strawberry_type
class Query:
    surveysStatus: list[SurveysStatus] = strawberry_field(resolver=query_surveys_status)


query_schema = Schema(query=Query)
