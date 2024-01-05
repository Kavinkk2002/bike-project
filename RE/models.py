from django.db import models

class kk(models.Model):
    Name=models.CharField(max_length=20,default="")
    Age=models.IntegerField(default="")
    Email=models.CharField(max_length=50,default="")
    Address=models.CharField(max_length=100,default="")

class kk1(models.Model):
    Name=models.CharField(max_length=20,default="")
    Age=models.IntegerField(default="")
    Department=models.CharField(max_length=20,default="")
    Address=models.CharField(max_length=100,default="")

class bd1(models.Model):
    Name=models.CharField(max_length=80,default="")
    Age=models.IntegerField(default="")
    City=models.CharField(max_length=150)
# Create your models here.
