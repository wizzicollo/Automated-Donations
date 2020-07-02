from rest_framework import serializers
from authentication.serializers import UserSerializer
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    
    bio = serializers.CharField(allow_blank=True, required=False)
    user = UserSerializer(read_only = True)

    class Meta:
        model = Profile
        fields = ( 'bio', 'image', 'user')