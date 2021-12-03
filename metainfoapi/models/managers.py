from django.db import models
from django.contrib.auth.models import User

class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    store = models.ForeignKey("Store", on_delete=models.CASCADE)