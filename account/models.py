from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone_number = models.IntegerField(blank=False)
    password = models.CharField(max_length=8, null=False)
    

    def __str__(self):
        return self.username