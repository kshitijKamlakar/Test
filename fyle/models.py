from tokenize import Token

from django.db import models

# Create your models here.
from rest_framework_simplejwt.state import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

class banks(models.Model) :
    name = models.CharField(max_length=49)
    id = models.BigIntegerField(primary_key=True)

class branches(models.Model):
    ifsc = models.CharField(max_length=11,primary_key=True)
    bank_id = models.ForeignKey(banks,on_delete= models.CASCADE)
    branch = models.CharField(max_length=74)
    address = models.CharField(max_length=195)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=26)

class bank_details(models.Model):
    ifsc = models.CharField(max_length=11,primary_key= True)
    bank_id = models.BigIntegerField()
    branch = models.CharField(max_length=74)
    address = models.CharField(max_length=195)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=26)
    bank_name = models.CharField(max_length=49)

    class Meta:
        managed = False
        db_table = 'bank_branches'