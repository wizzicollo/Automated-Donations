from rest_framework import serializers
# from Backend.authentication.serializers import  UserSerializer
# from .authentication.serializers import UserSerializer
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    bio = serializers.CharField(allow_blank=True, required=False)
    image = serializers.SerializerMethodField()
    # user = UserSerializer(read_only = True)

    class Meta:
        model = Profile
        fields = ('username', 'bio', 'image', 'user')
        read_only_fields = ('username',)

    def get_image(self, obj):
        if obj.image:
            return obj.image