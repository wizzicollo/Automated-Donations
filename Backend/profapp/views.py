from rest_framework import status
from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .exceptions import ProfileDoesNotExist
from .models import Profile
from .serializers import ProfileSerializer

class ProfileRetrieveAPIView(RetrieveUpdateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def perform_create(self, serializer):

        serializer.save(user=self.request.user) 