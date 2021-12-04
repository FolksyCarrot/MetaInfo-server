from django.db import models

class Projects(models.Model):
    employee = models.ForeignKey("Employee")
    customer = models.ForeignKey("Customer")
    store = models.ForeignKey("Store")
    description = models.TextField()
    budget = models.IntegerField()
    start = models.DateField()
    expected_completion = models.DateField()
    is_completed = models.BooleanField()