from email.policy import default
from django.db import models
from django.forms import IntegerField


class student(models.Model):
    name = models.CharField(max_length=50)
    tenth_uid = models.IntegerField()
    twelth_uid = models.IntegerField()
    aadhar_no = models.IntegerField()
    email_1 = models.CharField(max_length=50)
    phoneno = models.IntegerField()
    uni_roll = models.IntegerField()
    board = models.CharField(max_length=50)


def __str__(self):
    return self.name
