from django.db import models
import datetime

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    phone_number = models.IntegerField(max_length=15)
    password= models.CharField(max_length=500)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True, null=False)
    last_login = models.DateTimeField(default=datetime.datetime.now())
    role = models.ManyToManyField('Role' )
    permission = models.ManyToManyField('Permission')


class Role(models.Model):
    description = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    permission = models.ManyToManyField('Permission')

class Permission(models.Model):
    description = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
