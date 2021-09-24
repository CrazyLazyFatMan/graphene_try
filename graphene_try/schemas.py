from graphene import (
    ObjectType,
    Schema,
)

from business_app.queries import (
    Query as bq,
)
from business_app.mutations import (
    Mutation as bm
)


class Query(bq, ObjectType):
    pass


class Mutation(bm, ObjectType):
    pass


schema = Schema(query=Query, mutation=Mutation)
