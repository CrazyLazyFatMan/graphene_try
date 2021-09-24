from graphene import (
    Int,
    String,
)

from business_app.base.inputs import (
    BaseInput,
)


class BusinessInput(BaseInput):
    """Input for Business model"""

    name = String()
    employee_number = Int()
    address = String()
    founder = String()
