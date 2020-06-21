from django.db import models


# Create your models here.
class Story(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
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