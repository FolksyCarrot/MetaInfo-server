from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from metainfoapi.models import Employees
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from metainfoapi.models import Manager

class ManagerView(ViewSet):
    def list(self, request):
        managers = Manager.objects.all()
        serializer = ManagerSerializer(managers, many=True, context = {'request': request})
        return Response(serializer.data)
    
    def create(self, request):
        try:
            manager = Manager.objects.create(
               user = request.auth.user,
               store =  request.data["store"]
            )
            serializer = ManagerSerializer(manager, context = {'request': request})
            return Response({'message': 'manager created'}, status = status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)
            
    def retrieve(self, request, pk=None):
        try:
            manager = Manager.objects.get(pk=pk)
            serializer = ManagerSerializer(manager, context = {'request': request})
            return Response(serializer.data)
        except:
            return Response({'message': "Manager does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
    