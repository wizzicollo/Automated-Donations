from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
import datetime as dt




        
class Charity(models.Model):
    location = models.CharField(max_length=70, blank=False, default='')
    target_amount = models.PositiveIntegerField(default='1')
    amount_raised = models.PositiveIntegerField(default='1', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=False)
    
    



        
class Story(models.Model):
    charity = models.ForeignKey(Charity, on_delete=models.CASCADE,null=True)
    image = models.ImageField(upload_to='images/', blank=True)
    title = models.CharField(max_length=60)
    description = models.TextField()
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





  

