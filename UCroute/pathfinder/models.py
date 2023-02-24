from django.db import models


# Create your models here.
class Path(models.Model):
    starting_point = models.CharField(max_length=100)
    end_point = models.CharField(max_length=100)
    handicapped = models.BooleanField(default=False)

    def __str__(self):
        return self.starting_point


class Building(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

