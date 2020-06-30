from django.conf import settings
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from .models import Story
from .models import Charity
from .serializers import StoryMiniSerializer
from .serializers import CharityMiniSerializer
from .serializers import StorySerializer
from .serializers import CharitySerializer
from rest_framework import mixins
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view





class StoryViewset(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.UpdateModelMixin,mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    '''
    API endpoint that allows one to view posts created   
    '''
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    
    
    
    def list(self, request, *args, **kwargs):
        stories = Story.objects.all()
        serializer = StoryMiniSerializer(stories, many=True)
        return Response(serializer.data)
    


class CharityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Charity.objects.all()
    serializer_class = CharitySerializer
    
    def list(self, request, *args, **kwargs):
        charities = Charity.objects.all()
        serializer = CharityMiniSerializer(charities, many=True)
        return Response(serializer.data)