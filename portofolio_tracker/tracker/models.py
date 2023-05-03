# myapp/models.py
from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name