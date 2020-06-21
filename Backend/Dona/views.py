from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Donation
from .serializers import DonationSerializer
from rest_framework import mixins
\


class DonationViewset(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.UpdateModelMixin,mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    '''
    API endpoint that allows one to view the details of the donor
    '''
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer

