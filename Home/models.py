from django.db import models

# Create your models here.
class Register(models.Model):
    First_Name =models.CharField(max_length=50)
    Last_Name=models.CharField(max_length=50)
    Email=models.CharField(max_length=30)
    Password=models.CharField(max_length=20)
    Mobile=models.CharField(max_length=10)
    Gender=models.CharField(max_length=10)
    City=models.CharField(max_length=20)
    Worker_Type=models.CharField(max_length=20)
    Rate=models.CharField(max_length=20)