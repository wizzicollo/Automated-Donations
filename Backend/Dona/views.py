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


class CharityList(APIView):
    def get(self, request, format=None):
        all_charities = Charity.objects.all()
        serializers = CharitySerializer(all_charities, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = CharitySerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        charity = self.get_charity(pk)
        charity.delete()
        return JsonResponse({'message': '{} Charities were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

class CharityDetail(APIView):
    def get_charity(self, pk):
        try: 
            return Charity.objects.get(pk=pk)
        except Charity.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        charity = Charity.objects.get(pk=pk) 
        serializers = CharitySerializer(charity)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        charity = self.get_charity(pk)
        serializers = CharitySerializer(charity, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        charity = self.get_charity(pk)
        charity.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ApprovedCharities(APIView):

    def get(self, request, format=None):
        approved_charities = Charity.objects.filter(approved=True)
        serializers = CharitySerializer(approved_charities, many=True)
        return Response(serializers.data)