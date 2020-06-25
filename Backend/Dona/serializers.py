from rest_framework import serializers
from .models import Donation
from .models import Story
from .models import Donor
from Dona import models
from Dona.models import Charity

class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Donation


class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = '__all__'


class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Donor   



class CharitySerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Charity
        fields =  '__all__'    