from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    username = models.CharField(max_length=100, default='username')
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
class Student(models.Model):
    name = models.CharField(max_length=100)
    