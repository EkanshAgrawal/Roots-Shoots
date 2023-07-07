from django.db import models
from django.conf import settings

class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.IntegerField()
    message = models.TextField()