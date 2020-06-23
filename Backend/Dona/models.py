from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
import datetime as dt



class Donation(models.Model):
    currency= models.DecimalField(max_digits=6, decimal_places=2)
    amount = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    # currency = MoneyField(decimal_places=2, default=0, default_currency='USD', max_digits=11,)


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
    title = models.CharField(max_length=60)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/')
    image = models.URLField(blank=True)
    
    
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


class Donor(models.Model):
    name = models.CharField(max_length=60)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    location = models.CharField(max_length=50, default=None)
    description = models.TextField(null=True)
    organization = models.CharField(max_length=250, null=True)
    # phone_number = models.IntegerField(default=None)
    phone = PhoneNumberField(null=False, blank=False, unique=True,default=None)
    card_number = models.IntegerField(default=None)
        

    
    def __str__(self):
        return self.name

    def save_donor(self):
        self.save()

    def delete_donor(self):
        self.delete()

    def update_organization(cls,id,new_organization):
        cls.objects.filter(pk = id.update(organization=new_organization))
        new_organization_object = cls.objects.get(organization=new_organization)
        new_organization = new_organization_object.organization
        return new_organization


class Charity(models.Model):
    name = models.CharField(max_length=70, blank=False, default='')
    email = models.EmailField()
    description = models.TextField()
    location = models.CharField(max_length=70, blank=False, default='')
    # phone_number = models.CharField(max_length = 10,blank =True)
    phone = PhoneNumberField(null=False, blank=False, unique=True,default=None)
    target_amount = models.PositiveIntegerField()
    beneficiary = models.CharField(max_length=70, blank=False, default='')
    donors = models.CharField(max_length=70, blank=True )
    registration_date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)   

