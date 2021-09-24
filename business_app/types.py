from graphene_django.types import (
    DjangoObjectType,
)

from business_app.models import (
    Business,
)


class BusinessType(DjangoObjectType):

    class Meta:
        model = Business

