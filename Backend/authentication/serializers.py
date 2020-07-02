from rest_framework import serializers
from django.contrib.auth import authenticate
# from profapp.serializers import ProfileSerializer
from .models import User


class RegistrationSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True,
    )

    password2 = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True, label="Confirm password")

    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email',  'username', 'is_charity', 'password', 'password2', 'token']

    def create(self, validated_data):
        if validated_data.get('password') != validated_data.get('password2'):
            raise serializers.ValidationError(
                {"password": "The two passwords differ."})
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        return user



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    email = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        username = data.get('username', None)
        password = data.get('password', None)
        if username is None:
            raise serializers.ValidationError(
                'Username is required to log in.'
            )

        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )

        user = authenticate(username=username, password=password)

        if user is None:
            raise serializers.ValidationError(
                'A user with this username and password was not found.'
            )

        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )

        return {
            'email': user.email,
            'username': user.username,
            'token': user.token
        }


class UserSerializer(serializers.ModelSerializer):
    """Handles serialization and deserialization of User objects."""

    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )
    # profile = ProfileSerializer(write_only=True)
    bio = serializers.CharField(source='profile.bio', read_only=True)
    image = serializers.CharField(source='profile.image', read_only=True)


    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'token', 'profile', 'bio', 'image', 'is_charity')

        read_only_fields = ('token', 'is_charity')

    def update(self, instance, validated_data):
        """Performs an update on a User."""

        password = validated_data.pop('password', None)
        profile_data = validated_data.pop('profile', {})

        for (key, value) in validated_data.items():
            setattr(instance, key, value)

        if password is not None:
            instance.set_password(password)

        instance.save()

        for (key, value) in profile_data.items():
            setattr(instance.profile, key, value)
        instance.profile.save()

        return instance