from django.db import models


# Create your models here.
from django.contrib.auth.models import AbstractUser

# class User(AbstractUser):
#     pass#rollno = models.CharField(max_length=100)
    #sid=models.CharField(max_length=8)
class Register(AbstractUser):
    name = models.CharField(max_length=100)

class Logs(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
class Quest(models.Model):
    question = models.CharField(max_length=500)
    logid = models.CharField(max_length=500)
    status=models.CharField(max_length=1)
    users=models.CharField(max_length=100,default='unknwn')

    def __str__(self):
        return self.question

class Ans(models.Model):
    answer = models.CharField(max_length=500)
    questid = models.CharField(max_length=100)
    users=models.CharField(max_length=100,default='unknwn')
    #questid = models.ForeignKey(Quest,on_delete=models.CASCADE)
    status=models.CharField(max_length=1)
    def __str__(self):
        return self.answer
class Comm(models.Model):
    comment = models.CharField(max_length=500)
    ansid = models.CharField(max_length=50)
    users=models.CharField(max_length=100,default='unknwn')

    def __str__(self):
        return self.comment
