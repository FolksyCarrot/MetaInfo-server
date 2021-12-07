from django.db import models

class Projects(models.Model):
    employee = models.ForeignKey("Employees", on_delete=models.CASCADE)
    customer = models.ForeignKey("Customer", on_delete=models.CASCADE)
    store = models.ForeignKey("Store", on_delete=models.CASCADE)
    description = models.TextField()
    budget = models.IntegerField()
    start = models.DateField()
    expected_completion = models.DateField()
    is_completed = models.BooleanField()