from django.db import models

# Create your models here.

class Predictions(models.Model):
    age = models.CharField(max_length=3)
    fare = models.CharField(max_length=4)
    gender = models.CharField(max_length=7)
    pred = models.CharField(max_length=2)
