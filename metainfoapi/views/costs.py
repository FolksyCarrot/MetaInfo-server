from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from metainfoapi.models import ProjectCost
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError

from metainfoapi.models.projects import Projects

class Cost(ViewSet):
    
    def create(self, request):
        project = Projects.objects.get(pk=request.data['project_id'])
        try:
            cost = ProjectCost.objects.create(
               label = request.data['label'],
               cost = request.data['cost'],
               project_id = project
            )
            serializer = CostSerializer(cost, context = {'request': request})
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)
        
    def list(self, request):
        project = Projects.objects.get(pk=request.data['project_id'])
        cost = ProjectCost.objects.all()
        serializer = CostSerializer(cost, context = {'request': request})
        return Response(serializer.data, status= status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        try: 
            cost = ProjectCost.objects.get(pk=pk)
            serializer = CostSerializer(cost, context = {'request': request})
            return Response(serializer.data)
        except:
            return Response(status= status.HTTP_204_NO_CONTENT)
        
    def update(self, request, pk=None):
        project = Projects.objects.get(pk=request.data['project_id'])
        try:
            cost = ProjectCost.objects.get(pk=pk)
            cost.label = request.data['label']
            cost.cost = request.data['cost']
            cost.project_id = project
            cost.save()
            return Response({'message': 'cost updated'}, status= status.HTTP_204_NO_CONTENT)
        except:
            return Response({'message': 'cost not found'}, status= status.HTTP_404_NOT_FOUND)
        
    def destroy(self, request, pk=None):
        
        try:
            cost = ProjectCost.objects.get(pk=pk)
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except ProjectCost.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
class CostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectCost
        fields = ('label', 'cost', 'project')