from graphene import (
    Boolean,
    Field,
    Int,
    Mutation,
    ObjectType,
    List,
    String,
)
from graphene.types.generic import GenericScalar

from business_app.inputs import (
    BusinessInput,

)
from business_app.models import (
    Business,
)
from business_app.types import (
    BusinessType,
)


class CreateBusiness(Mutation):
    """Mutation for creating Business model instances"""
    class Arguments:
        input_data = BusinessInput(required=True)

    ok = Boolean()
    business = Field(BusinessType)

    @staticmethod
    def mutate(root, info, input_data=None):
        ok = True

        business_instance = Business(
            name=input_data.name,
            employee_number=input_data.employee_number,
            address=input_data.address,
            founder=input_data.founder,
        )
        business_instance.save()

        return CreateBusiness(ok=ok, business=business_instance)


class UpdateBusiness(Mutation):
    """Mutation for updating Business model instances"""

    class Arguments:
        instance_id = Int(required=True)
        input_data = BusinessInput(required=True)

    ok = Boolean()
    business = Field(BusinessType)

    @staticmethod
    def mutate(root, info, instance_id, input_data=None):
        ok = False
        business_instance = Business.objects.get(id=instance_id)
        if business_instance:
            ok = True
            business_instance.name = input_data.name
            business_instance.employee_number = input_data.employee_number
            business_instance.address = input_data.address
            business_instance.founder = input_data.founder
            business_instance.save()

        return UpdateBusiness(ok=ok, business=business_instance)


class DeleteBusiness(Mutation):
    """Mutation for deleting Business model instances"""

    class Arguments:
        instance_ids = List(required=True, of_type=Int)

    ok = Boolean()
    business = Field(BusinessType)

    @staticmethod
    def mutate(root, info, instance_ids):
        ok = False
        businesses = []
        for b_id in instance_ids:
            try:
                ok = True
                business_instance = Business.objects.get(id=b_id)
                business_instance.delete()
                businesses.append(business_instance)
            except Business.DoesNotExist:
                ok = False
                break
        return DeleteBusiness(ok=ok, business=businesses)


class Mutation(ObjectType):
    create_business = CreateBusiness.Field()
    update_business = UpdateBusiness.Field()
    delete_business = DeleteBusiness.Field()
