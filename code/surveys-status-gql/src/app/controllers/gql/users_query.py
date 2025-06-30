from typing import Optional

from app.models.gql.users import User


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
