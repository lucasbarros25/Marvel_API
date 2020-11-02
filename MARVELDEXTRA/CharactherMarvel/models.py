from django.db import models

# Create your models here.

class Characther(models.Model):
    name = models.CharField(max_length=100)
    comics = models.TextField()
    events = models.TextField()
    series = models.TextField()
    stories = models.TextField()


