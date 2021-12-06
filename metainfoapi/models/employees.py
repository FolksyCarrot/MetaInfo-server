from django.db import models

class Employees(models.Model):
    name = models.CharField(max_length=30)
    position = models.CharField(max_length=30)
    salary = models.IntegerField()