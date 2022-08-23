from time import time
from django.db import models

class StickynoteInput(models.Model):
    name = models.CharField(max_length=3000)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now=True)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name