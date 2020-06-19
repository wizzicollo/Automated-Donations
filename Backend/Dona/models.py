from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Donor(models.Model):
    name = models.CharField(max_length=60)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    location = models.CharField(max_length=50, default=None)
    description = models.TextField(null=True)
    organization = models.CharField(max_length=250, null=True)
    phone_number = models.IntegerField(default=None)
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