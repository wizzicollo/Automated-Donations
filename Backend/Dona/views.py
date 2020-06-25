from django.conf import settings
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from .models import Donation
from .models import Story
from .models import Donor
from .models import Charity
from .serializers import DonationSerializer
from .serializers import DonorSerializer
from .serializers import StorySerializer
from .serializers import CharitySerializer
from rest_framework import mixins
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view




class DonationViewset(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.UpdateModelMixin,mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    '''
    API endpoint that allows one to view the details of the donation
    '''
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer


class StoryViewset(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.UpdateModelMixin,mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    '''
    API endpoint that allows one to view posts created   
    '''
    queryset = Story.objects.all()
    serializer_class = StorySerializer


class DonorViewset(viewsets.ModelViewSet):
    '''
    API endpoint that allows one to view the details of the donor
    '''
    queryset = Donor.objects.all()
    serializer_class = DonorSerializer    


class CharityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Charity.objects.all()
    serializer_class = CharitySerializer