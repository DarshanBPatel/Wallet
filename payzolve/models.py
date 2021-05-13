from django.db import models

# Create your models here.


class wallet(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60, default=" ")
    mobile_number = models.CharField(max_length=10, unique=True)
    balance = models.IntegerField(default=100)
    password = models.CharField(max_length=10)
