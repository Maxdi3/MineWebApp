from django.db import models

# Create your models here.


class Users(models.Model):
    name = models.CharField(max_length=32, null=False, blank=False)
    machine_name = models.CharField(max_length=32, null=False, blank=False)
    location_long = models.CharField(max_length=32, null=False, blank=False)
    location_lat = models.CharField(max_length=32, null=False, blank=False)
    status = models.IntegerField(default=0)
    icon = models.IntegerField(default=0)
    last_update = models.DateTimeField()

