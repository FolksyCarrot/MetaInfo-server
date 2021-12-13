from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from metainfoapi.models import Employees, Manager, Store
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from metainfoapi.models.store_employees import StoreEmployees

from metainfoapi.models.stores import Store

class EmployeeView(ViewSet):
    
    def list(self, request):
        store_id = self.request.query_params.get("store_id", None)
        employees = Employees.objects.all()
        if store_id is not None:
            employees = employees.filter(store_employee__id = store_id)
        serializer = EmployeeSerializer(employees, many=True, context={'request': request})
        return Response(serializer.data)
    
    def retrieve(self, request, pk):
        try:
            employees = Employees.objects.get(pk=pk)
            serializer = EmployeeSerializer(employees, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    def create(self, request):
        manager = Manager.objects.get(user = request.auth.user)
        store = Store.objects.get(pk=manager.store.id)
        
        try:
            employee = Employees.objects.create(
                name = request.data['name'],
                position = request.data['position'],
                salary = request.data['salary']
            )
            employee.store_employee.set([store.id])
            serializer = EmployeeSerializer(employee, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)
        
    def update(self, request, pk=None):
        employee = Employees.objects.get(pk=pk)
        employee.name = request.data['name']
        employee.position = request.data['position']
        employee.salary = request.data['salary']
        employee.save()
        return Response({'message': 'employee updated'}, status = status.HTTP_204_NO_CONTENT)
    
    
            


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model= Store
        fields = ('name', 'id')      
         
class EmployeeSerializer(serializers.ModelSerializer):
    store_employee = StoreSerializer(many=True)
    class Meta:
        model = Employees
        fields = ('name', 'position', 'salary', 'store_employee')