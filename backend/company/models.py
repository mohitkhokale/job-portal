from django.db import models

class Company(models.Model):
    username = models.CharField(max_length=255)
    name = models.CharField(max_length=155)
    website =models.CharField(max_length=155)
    phoneNumber = models.PositiveIntegerField
    address = models.CharField(max_length=155)
    city =  models.CharField(max_length=55)
    state =  models.CharField(max_length=55)
    country =  models.CharField(max_length=55)
    industryList =  models.CharField(max_length=155)

    def __str__(self) -> str:
        return str(self.name)

