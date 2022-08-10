from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    age = models.IntegerField(null=True, default=0)
    phone_number = models.CharField(max_length=12, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)


class Supplier(models.Model):
    name = models.CharField(max_length=100)
    manager_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    address = models.CharField(max_length=150)


# class User(models.Model):
#   username = models.CharField(max_length=100)
#  first_name = models.CharField(max_length=100)
# last_name = models.CharField(max_length=100)
# email_address = models.EmailField(max_length=100)
# password = models.CharField(max_length=50)
# age = models.IntegerField()
# phone_number = models.IntegerField()
# address = models.CharField(max_length=100)
