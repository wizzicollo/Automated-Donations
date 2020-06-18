from django.db import models
import datetime as dt

# Create your models here.
class Charity(models.Model):
    name = models.CharField(max_length=70, blank=False, default='')
    email = models.EmailField()
    description = models.TextField()
    location = models.CharField(max_length=70, blank=False, default='')
    phone_number = models.CharField(max_length = 10,blank =True)
    target_amount = models.PositiveIntegerField()
    beneficiary = models.CharField(max_length=70, blank=False, default='')
    donors = models.CharField(max_length=70, blank=True )
    registration_date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)