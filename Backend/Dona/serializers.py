from rest_framework import serializers 
from Dona.models import Charity

class CharitySerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Charity
        fields = ('name',
        'email',
        'description',
        'location',
        'phone_number',
        'target_amount',
        'beneficiary',
        'donors',
        'registration_date',
        'approved',)
        