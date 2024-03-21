from django.db import models

class class_models(models.Model):
    name = models.CharField(max_length=200)
    batch = models.CharField(max_length=10)
    age = models.IntegerField()
