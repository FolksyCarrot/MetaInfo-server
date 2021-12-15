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
    @property
    def totalCost(self):
        cost = self.projectcost_set.all()
        total = 0
        for expense in cost:
            total += expense.cost
            
        return total