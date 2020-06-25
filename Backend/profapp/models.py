from django.db import models


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True
        ordering = ["-created_at","-updated_at" ]


class Profile(TimestampedModel):
    user = models.OneToOneField(
        'authentication.User', on_delete=models.CASCADE
    )
    bio = models.TextField(blank=True)
    image = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class Charity(models.Model):
    location = models.CharField(max_length =10, null=True, blank=True, default= 'kilimani')
    target = models.CharField(max_length =50, null=True, blank=True, default= 'lower class')
    amount_raise = models.DecimalField(default = 0.00, decimal_places=2, max_digits=1000)
    

