from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Donor
from .serializer import DonorSerializer




class DonorViewset(viewsets.ModelViewSet):
    '''
    API endpoint that allows one to view the details of the donor
    '''
    queryset = Donor.objects.all()
    serializer_class = DonorSerializer    




