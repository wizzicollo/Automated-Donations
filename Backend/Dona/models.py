from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from authentication.models import *
from Donations import settings
import datetime as dt



class Donor(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,  default=None)
  
        
class Charity(models.Model):
    location = models.CharField(max_length=70, blank=False, default='')
    target_amount = models.PositiveIntegerField(default='1')
    amount_raised = models.PositiveIntegerField(default='1', blank=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    # user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,  default=None)

    # def __str__(self):
    #     return self.name

class Donation(models.Model):
    donor_id = models.ForeignKey(Donor, on_delete=models.CASCADE ,default='1', blank=True)
    charity_id = models.ForeignKey(Charity, on_delete=models.CASCADE ,default='1', blank=True)
    amount = models.PositiveIntegerField()
    reminder = models.DurationField()
    card_number = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True )
 

    def __str__(self):
        return self.name
    def save_donation(self):
        self.save()
    def delete_donation(self):
        self.delete()
    def update_donation(cls,id,new_donation):
        cls.objects.filter(pk = id.update(donation=new_donation))
        new_donation_object = cls.objects.get(donation=new_donation)
        new_donation = new_donation_object.donation
        return new_donation

        
class Story(models.Model):
    charity_id = models.ForeignKey(Charity, on_delete=models.CASCADE ,default='1', blank=True)
    title = models.CharField(max_length=60)
    description = models.TextField()
    story_image = models.ImageField(upload_to='story/', blank=True)
    location = models.CharField(max_length=20)

        
    def __str__(self):
        return self.title
    
    def save_story(self):
        self.save()
        
    def delete_story(self):
        self.delete()
        
    def update_story(cls,id,new_story):
        cls.objects.filter(pk = id.update(story=new_story))
        new_story_object = cls.objects.get(story=new_story)
        new_story = new_story_object.story
        
        return new_story





  

