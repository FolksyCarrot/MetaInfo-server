from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from metainfoapi.models import ProjectCost, Projects

class CostsTests(APITestCase):
    def setup(self):
        