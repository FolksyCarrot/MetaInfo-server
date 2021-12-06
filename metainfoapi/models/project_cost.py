from django.db import models

class ProjectCost(models.Model):
    label = models.CharField(max_length=30)
    cost = models.IntegerField()
    project = models.ForeignKey("Project")
    
    # store = models.ForeignKey("Store")