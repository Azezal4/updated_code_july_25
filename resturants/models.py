from django.db import models


class ResturantLocation(models.Model):
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=120, null=True, blank=True)

    category = models.CharField(max_length=120, null= True, blank= True)
    timestamp = models.DateTimeField(auto_now_add=True)

# Create your models here.
