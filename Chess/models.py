from django.db import models

class Chess(models.Model):
    title = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    notes = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    image = models.CharField(max_length=100)