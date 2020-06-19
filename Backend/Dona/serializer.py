from rest_framework import serializers
from .models import Donor
from Dona import models

class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Donor