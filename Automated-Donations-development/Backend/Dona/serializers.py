from rest_framework import serializers
from .models import Story
from Dona.models import Charity



class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = '__all__'

class StoryMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = '__all__'
        


class CharitySerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Charity
        fields =  '__all__'    