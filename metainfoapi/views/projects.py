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
from metainfoapi.views.costs import CostSerializer

class ProjectView(ViewSet):
    def create(self, request):
        try: 
            manager = Manager.objects.get(user = request.auth.user)
            store = Store.objects.get(pk=manager.store.id)
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
        store = Store.objects.get(pk=manager.store.id)
        projects = Projects.objects.filter(store = store)
        for project in projects:
            project.cost = project.projectcost_set.all()
        serializer = ProjectSerializer(projects, many=True, context = {'request': request})
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        try:
            project = Projects.objects.get(pk=pk)
            project.cost = project.projectcost_set.all()
            serializer = ProjectSerializer(project, many = False, context = {'request': request})
            return Response(serializer.data)
        except: 
            return Response("project does not exist", status=status.HTTP_404_NOT_FOUND)
        
    def update(self, request, pk=None):
        is_completed = f'{request.data["is_completed"]}'
        manager = Manager.objects.get(user = request.auth.user)
        store = Store.objects.get(pk=manager.store.id)
        project = Projects.objects.get(pk=pk)
        project.employee = project.employee
        project.customer = project.customer
        project.store = project.store
        project.description = request.data['description']
        project.budget = request.data['budget']
        project.start = request.data['start']
        project.expected_completion = request.data['expected_completion']
        if is_completed.lower() == 'true':
            project.is_completed = True
        else:
            project.is_completed = False
        project.save()
        return Response({'message': 'project updated'}, status = status.HTTP_204_NO_CONTENT)
    
class ProjectSerializer(serializers.ModelSerializer):
    cost = CostSerializer(many =True, required=False)
    class Meta:
        model = Projects
        fields = ('id', 'employee', 'customer', 'store', 'description', 'budget', 'start', 'expected_completion', 'is_completed', 'cost', 'totalCost')
        depth = 1