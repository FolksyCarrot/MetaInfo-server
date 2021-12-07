from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from metainfoapi.models import Projects
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from django.contrib.auth.models import User
from metainfoapi.models.customers import Customer
from metainfoapi.models.employees import Employees

from metainfoapi.models.managers import Manager
from metainfoapi.models.stores import Store

class ProjectView(ViewSet):
    def create(self, request):
        try: 
            manager = Manager.objects.get(user = request.auth.user)
            store = Store.objects.get(pk=manager.store)
            employee = Employees.objects.get(pk = request.data['employee_id'])
            customer = Customer.objects.get(pk = request.data['customer'])
            project = Projects.objects.create(
                employee = employee,
                customer = customer,
                store = store,
                description = request.data['description'],
                budget = request.data['budget'],
                start = request.data['start'],
                expected_completion = request.data['expected_completion'],
                is_completed = request.data['is_completed']
            )
            
            serializer = ProjectSerializer(project, context = {'request': request})
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)
        
    def list(self, request):
        manager = Manager.objects.get(user = request.auth.user)
        store = Store.objects.get(pk=manager.store)
        store.project = store.project_set.all()
        serializer = ProjectSerializer(store, many=True, context = {'request': request})
        return Response(serializer.data)