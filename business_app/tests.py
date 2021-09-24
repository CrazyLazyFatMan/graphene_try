import pytest
import os

from django.test import (
    TestCase,
)
from mixer.backend.django import (
    mixer,
)
from graphene.test import (
    Client
)

from graphene_try.schemas import (
    schema,
)
from business_app.models import (
    Business,
)
from business_app.test_mutations import (
    create_mutation,
    delete_mutation,
    update_mutation,
)
from business_app.test_queries import (
    get_many_query,
    get_one_query,
)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "graphene_try.settings")


@pytest.mark.django_db
class Test(TestCase):

    def setUp(self):
        self.client = Client(schema)
        self.client.execute(create_mutation)
        self.business = mixer.blend(Business)
        self.default_id = 1

    def test_create(self):
        test_name = "JK Furman und Young"
        response = self.client.execute(create_mutation)
        response_business = response.get('data').get('createBusiness').get('business')
        business_name = response_business.get('name')
        assert business_name == test_name

    def test_get_one_business(self):
        response = self.client.execute(get_one_query)
        response_business = response.get('data').get('business')
        business_id = int(response_business.get('id'))
        assert business_id == self.default_id

    def test_update_business(self):
        response = self.client.execute(update_mutation)
        print(response)

    def test_get_many_businesses(self):
        response = self.client.execute(get_many_query)
        response_businesses = response.get('data').get('businesses')
        assert response_businesses is not None and len(response_businesses) > 1

    def test_delete_businesses(self):
        response = self.client.execute(delete_mutation)
        result = response.get('data').get('deleteBusiness').get('ok')
        assert result
