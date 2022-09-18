from django.test import TestCase
from rest_framework.test import APIRequestFactory


class APPViewTest(TestCase):
    
    factory = APIRequestFactory()
    request = factory.post('/', {"payload": "new payload"}, format='json')
