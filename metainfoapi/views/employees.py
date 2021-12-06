from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from metainfoapi.models import Employees
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError

from metainfoapi.models.stores import Store

class EmployeeView(ViewSet):
    
    def list(self, request):
        employees = Employees.objects.all()
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
        try:
            employee = Employees.objects.create(
                name = request.data['name']
                position = request.data['position'],
                salary = request.data['salary']
            )
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
    
    def destroy(self, request, pk=None):
        try:
            employee= Employees.objects.get(pk=pk)
            employee.delete()
            return Response({'message': 'employee deleted'}, status=status.HTTP_204_NO_CONTENT)
        except Employees.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'
        
class EmployeeSerializer(serializers.ModelSerializer):
    store = StoreSerializer()
    class Meta:
        model = Employees
        fields = ('name', 'position', 'salary', 'store')