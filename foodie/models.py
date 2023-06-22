from django.db import models

# Create your models here.
class Foodie(models.Model):
    name = models.CharField(max_length=150)
    location = models.TextField()
    items = models.TextField()
    lat_long = models.TextField()
    full_details = models.TextField()

    def __str__(self):
        return self.name