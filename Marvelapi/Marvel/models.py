from django.db import models

# Create your models here.

class Character(models.Model):
    name = models.CharField(max_length=100)
    comics = models.ForeignKey('Comics', on_delete=models.CASCADE)
    events = models.ForeignKey('Event', on_delete=models.CASCADE)
    series = models.ForeignKey('Series', on_delete=models.CASCADE)
    stories = models.ForeignKey('Stories', on_delete=models.CASCADE)


class Comics(models.Model):
    comics = models.CharField(max_length=100)
    status = models.CharField(max_length=100)    

class Event(models.Model):
    events = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

class Series(models.Model):
    series = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

class Stories(models.Model):
    stories = models.CharField(max_length=100)
    status = models.CharField(max_length=100)