from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from metainfoapi.models import Customer
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError

from metainfoapi.models.managers import Manager

class CustomerView(ViewSet):
    
    def create(self, request):
        try:
            customer = Customer.objects.create(
                name = request.data['name']
            )
            serializer = CustomerSerializer(customer, context = {'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    def list(self, request):
        # manager = Manager.objects.get(user = request.auth.user)
        customer = Customer.objects.all()
        # customers = customer.objects.filter(customer__store)
        serializer = CustomerSerializer(customer, many=True, context = {'request': request})
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        customer = Customer.objects.get(pk=pk)
        serializer = CustomerSerializer(customer, context = {'request': request})
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        customer = Customer.objects.get(pk=pk)
        customer.name= request.data['name']
        
        customer.save()
        return Response({}, status=status.HTTP_204_NO_CONTENT)
    
class CustomerSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'