from django.db import models

# Create your models here.

class ComplantDetails(models.Model):
    name = models.CharField(max_length=30, null=False)
    phone_number = models.IntegerField(blank=False)
    state = models.CharField(null=False, blank=False)
    address = models.CharField(max_length=1000, null=False, blank=False)

    def __str__(self):
        return self.name
