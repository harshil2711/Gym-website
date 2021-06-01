from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    place = models.CharField(max_length=50)
    message = models.CharField(max_length=500)
    date = models.DateField()

    def __str__(self):
        return self.name
    

class Registration(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    phone = models.IntegerField()
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    date = models.DateField()

    def __str__(self):
        return self.name
    