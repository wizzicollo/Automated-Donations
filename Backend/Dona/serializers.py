from rest_framework import serializers 
from Dona.models import Charity

class CharitySerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Charity
        fields = '__all__'
        