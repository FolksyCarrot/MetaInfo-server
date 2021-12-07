from django.db import models

class ProjectCost(models.Model):
    label = models.CharField(max_length=100)
    cost = models.IntegerField()
    project = models.ForeignKey("Projects", on_delete=models.CASCADE)
    
    # store = models.ForeignKey("Store")