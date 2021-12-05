from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from metainfoapi.models import Employees

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
            

    
    
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'