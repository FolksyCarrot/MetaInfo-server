from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from metainfoapi.models import Store
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError

from metainfoapi.models.employees import Employees


class StoreView(ViewSet):
    
    def list(self, request):
        stores = Store.objects.all()
        serializer = StoreSerializer(stores, many=True, context = ({'request': request}))
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        try:
            store = Store.objects.get(pk=pk)
            serializer = StoreSerializer(store, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields= '__all__'    
        
class StoreSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer()
    class Meta:
        model = Store
        fields = ('name', 'location', 'employee')