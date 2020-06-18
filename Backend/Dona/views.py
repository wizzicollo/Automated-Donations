from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from Dona.models import Charity
from Dona.serializers import CharitySerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST', 'DELETE'])
def charities_list(request):
    # GET list of charities, POST a new charities, DELETE all charities

    if request.method == 'GET':
        charities = Charity.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            charities = charities.filter(title__icontains=title)
        
        charities_serializer = CharitySerializer(charities, many=True)
        return JsonResponse(charities_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        charity_data = JSONParser().parse(request)
        charity_serializer = CharitySerializer(data=charity_data)
        if charity_serializer.is_valid():
            charity_serializer.save()
            return JsonResponse(charity_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(charity_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Charity.objects.all().delete()
        return JsonResponse({'message': '{} Charities were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def charity_detail(request, pk):
    # find charity by pk (id)
    try: 
        charity = Charity.objects.get(pk=pk) 
    
    
    except Charity.DoesNotExist: 
        return JsonResponse({'message': 'The Charity does not exist'}, status=status.HTTP_404_NOT_FOUND) 

    if request.method == 'GET': 
        charity_serializer = CharitySerializer(charity) 
        return JsonResponse(charity_serializer.data) 
       
    elif request.method == 'PUT': 
        charity_data = JSONParser().parse(request) 
        charity_serializer = CharitySerializer(charity, data=charity_data) 
        if charity_serializer.is_valid(): 
            charity_serializer.save() 
            return JsonResponse(charity_serializer.data) 
        return JsonResponse(charity_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    elif request.method == 'DELETE': 
        charity.delete() 
        return JsonResponse({'message': 'Charity was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
 

@api_view(['GET'])
def approved_charities_list(request):
    # GET all published charities
    charities = Charity.objects.filter(approved=True)
        
    if request.method == 'GET': 
        charities_serializer = CharitySerializer(charities, many=True)
        return JsonResponse(charities_serializer.data, safe=False)