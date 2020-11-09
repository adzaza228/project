from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class gun(models.Model):
    name = models.CharField(max_length=15)
    coliber = models.FloatField(default=0)
    make_country = models.CharField(max_length=15)
    year_invented = models.IntegerField(default=0)

class block(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField()

