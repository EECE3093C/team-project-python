from django.db import models


# Create your models here.
class Path(models.Model):
    starting_point = models.CharField(max_length=100, default='')
    end_point = models.CharField(max_length=100, default='')
    distance = models.CharField(max_length=100, default='')
    handicapped = models.BooleanField(default=False)
    obstructed = models.BooleanField(default=False)

    def __str__(self):
        return self.starting_point


class Building(models.Model):
    name = models.CharField(max_length=200, default='')
    location = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.name


class Entrances(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE, default=None)
    location = models.CharField(max_length=100, default='')
    handicapped = models.BooleanField(default=False)
    obstructed = models.BooleanField(default=False)

