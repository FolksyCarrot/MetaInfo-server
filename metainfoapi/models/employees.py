from django.db import models

class Employees(models.Model):
    position = models.CharField(max_length=30)
    salary = models.IntegerField()