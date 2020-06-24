from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Donation
from .serializers import DonationSerializer
from rest_framework import mixins


from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Story
from .serializers import StorySerializer
from rest_framework import mixins



from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Donor
from .serializers import DonorSerializer



from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.views import APIView
from .models import Charity
from .serializers import CharitySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response



from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.views import APIView
from .models import Charity
from .serializers import CharitySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets


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
    queryset = Charity.objects.all().order_by('name')
    serializer_class = CharitySerializer