from django.db import models


# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass#rollno = models.CharField(max_length=100)
    #sid=models.CharField(max_length=8)
class Register(models.Model):
    name = models.CharField(max_length=100)
    rollno = models.CharField(max_length=100)
    sid=models.CharField(max_length=8)
class Logs(models.Model):
    nam = models.CharField(max_length=100)
    sid = models.CharField(max_length=100)
class Quest(models.Model):
    question = models.CharField(max_length=500)
    logid = models.ForeignKey(Logs,on_delete=models.CASCADE)
    status=models.CharField(max_length=1)

    def __str__(self):
        return self.question
class Ans(models.Model):
    answer = models.CharField(max_length=500)
    questid = models.CharField(max_length=50)
    # userid = models.ForeignKey(Logs,on_delete=models.CASCADE)
    status=models.CharField(max_length=1)
