from django.db import (
    models,
)

from business_app.base.models import (
    BaseModel,
)


class Business(BaseModel):
    """Model for info about business"""
    name = models.CharField(max_length=100)
    employee_number = models.IntegerField(null=False)
    address = models.CharField(max_length=100)
    founder = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'graph_business'
