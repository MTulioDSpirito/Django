

from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    
    email = models.EmailField()
    
    senha= models.CharField(max_length=128)
