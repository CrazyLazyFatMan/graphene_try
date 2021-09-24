from graphene import (
    Boolean,
    Field,
    Int,
    List,
    ObjectType,
)

from business_app.models import (
    Business,
)

from business_app.types import (
    BusinessType,
)


class Query(ObjectType):
    """Query for resolving Business instances by one or by many objects"""

    business = Field(BusinessType, id=Int())
    businesses = List(BusinessType)

    def resolve_business(self, info, **kwargs):
        business_id = kwargs.get('id')
        result = None

        if business_id is not None:

            result = Business.objects.get(id=business_id)

        return result

    def resolve_businesses(self, info, **kwargs):

        return Business.objects.all()
