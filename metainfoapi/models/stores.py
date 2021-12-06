from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    employees = models.ManyToManyField('Employees', through = 'StoreEmployees', related_name='store_employee')