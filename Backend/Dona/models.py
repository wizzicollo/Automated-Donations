from django.db import models
from django.contrib.auth.models import User
# Create your models here.
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

