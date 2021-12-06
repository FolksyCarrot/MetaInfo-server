from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from metainfoapi.models import Store
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError


class StoreView(ViewSet):
    
    def list(self, request):
        stores = Store.objects.all()
        serializer = StoreSerializer(stores, many=True, context = ({'request': request}))
        return Response(serializer.data)
        
        
        
class StoreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Store
        fields = '__all__'