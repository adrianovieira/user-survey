from app.models.gql.query import query_schema
from strawberry.fastapi import GraphQLRouter

graphql_router = GraphQLRouter(query_schema)
