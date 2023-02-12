from django.db import models

# Create your models here.


class Student(models.Model):
    roll = models.IntegerField()
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    marks = models.FloatField()
    mail = models.EmailField()
    address = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    c_password = models.CharField(max_length=30)
