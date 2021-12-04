from django.db import models

class StoreEmployees(models.Model):
    employee = models.ForeignKey("Employee", on_delete=models.CASCADE)
    store = models.ForeignKey("Store", on_delete=models.CASCADE)