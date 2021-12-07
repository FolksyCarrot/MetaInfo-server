from django.db import models

class StoreEmployees(models.Model):
    employee = models.ForeignKey("Employees", on_delete=models.CASCADE)
    store = models.ForeignKey("Store", on_delete=models.CASCADE)