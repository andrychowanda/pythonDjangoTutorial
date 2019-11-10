from django.db import models

class User(models.Model):
    userName = models.CharField(primary_key=True, max_length=100)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    dob = models.DateField()
    phoneNumber = models.IntegerField()
