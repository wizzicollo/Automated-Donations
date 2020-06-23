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

class CharityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Charity.objects.all().order_by('name')
    serializer_class = CharitySerializer

# class CharityList(APIView):
#     def get(self, request, format=None):
#         all_charities = Charity.objects.all()
#         serializers = CharitySerializer(all_charities, many=True)
#         return Response(serializers.data)

#     def post(self, request, format=None):
#         serializers = CharitySerializer(data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data, status=status.HTTP_201_CREATED)
#         return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         charity = self.get_charity(pk)
#         charity.delete()
#         return JsonResponse({'message': '{} Charities were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

# class CharityDetail(APIView):
#     def get_charity(self, pk):
#         try: 
#             return Charity.objects.get(pk=pk)
#         except Charity.DoesNotExist:
#             return Http404

#     def get(self, request, pk, format=None):
#         charity = Charity.objects.get(pk=pk) 
#         serializers = CharitySerializer(charity)
#         return Response(serializers.data)

#     def put(self, request, pk, format=None):
#         charity = self.get_charity(pk)
#         serializers = CharitySerializer(charity, request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data)
#         else:
#             return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         charity = self.get_charity(pk)
#         charity.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class ApprovedCharities(APIView):

#     def get(self, request, format=None):
#         approved_charities = Charity.objects.filter(approved=True)
#         serializers = CharitySerializer(approved_charities, many=True)
#         return Response(serializers.data)



# @api_view(['GET', 'POST', 'DELETE'])
# def charities_list(request):
#     # GET list of charities, POST a new charities, DELETE all charities

#     if request.method == 'GET':
#         charities = Charity.objects.all()
        
#         title = request.GET.get('title', None)
#         if title is not None:
#             charities = charities.filter(title__icontains=title)
        
#         charities_serializer = CharitySerializer(charities, many=True)
#         return JsonResponse(charities_serializer.data, safe=False)
#         # 'safe=False' for objects serialization

#     elif request.method == 'POST':
#         charity_data = JSONParser().parse(request)
#         charity_serializer = CharitySerializer(data=charity_data)
#         if charity_serializer.is_valid():
#             charity_serializer.save()
#             return JsonResponse(charity_serializer.data, status=status.HTTP_201_CREATED) 
#         return JsonResponse(charity_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         count = Charity.objects.all().delete()
#         return JsonResponse({'message': '{} Charities were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET', 'PUT', 'DELETE'])
# def charity_detail(request, pk):
#     # find charity by pk (id)
#     try: 
#         charity = Charity.objects.get(pk=pk) 
    
    
#     except Charity.DoesNotExist: 
#         return JsonResponse({'message': 'The Charity does not exist'}, status=status.HTTP_404_NOT_FOUND) 

#     if request.method == 'GET': 
#         charity_serializer = CharitySerializer(charity) 
#         return JsonResponse(charity_serializer.data) 
       
#     elif request.method == 'PUT': 
#         charity_data = JSONParser().parse(request) 
#         charity_serializer = CharitySerializer(charity, data=charity_data) 
#         if charity_serializer.is_valid(): 
#             charity_serializer.save() 
#             return JsonResponse(charity_serializer.data) 
#         return JsonResponse(charity_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
#     elif request.method == 'DELETE': 
#         charity.delete() 
#         return JsonResponse({'message': 'Charity was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
 

# @api_view(['GET'])
# def approved_charities_list(request):
#     # GET all published charities
#     charities = Charity.objects.filter(approved=True)
        
#     if request.method == 'GET': 
#         charities_serializer = CharitySerializer(charities, many=True)
#         return JsonResponse(charities_serializer.data, safe=False)