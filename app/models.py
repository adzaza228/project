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


class article(models.Model):
    name = models.CharField(max_length=150)
    clarification = models.CharField(max_length=150)
    href_view = models.CharField(max_length=150)


class book(models.Model):
    name = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    short_description = models.CharField(max_length=150)
    long_description = models.CharField(max_length=1500)
    image = models.ImageField()
    price = models.IntegerField()


class cart(models.Model):
    href_user = models.ForeignKey(User, on_delete=models.CASCADE)
    many_to_many_field = models.ManyToManyField(book, max_length=100)


