from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch  import receiver
from cloudinary.models import CloudinaryField

class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True
        ordering = ["-created_at","-updated_at" ]


class Profile(TimestampedModel):
    user = models.OneToOneField(
        'authentication.User', primary_key=True, on_delete=models.CASCADE
    )
    bio = models.TextField(blank=True)
    image = CloudinaryField()
    story_image = models.ImageField(upload_to='profiles/', blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'


    class Meta:
        db_table = 'profile'

    @receiver(post_save, sender=User)
    def update_create_profile(sender,instance,created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()


    def save_profile(self):
        self.save()

        