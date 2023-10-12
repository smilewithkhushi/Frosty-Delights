from django.db import models

# Create your models here.
class Contact(models.Model):
    username = models.CharField(max_length=30)
    #charfield is similar to varchar
    email = models.CharField(max_length=40)
    brand = models.CharField(max_length=20)
    flavour = models.CharField(max_length=20)
    extraInformation = models.TextField()
    date = models.DateField()