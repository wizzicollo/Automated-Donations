# from django.shortcuts import render
# from django.http import JsonResponse

# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .serializers import StorySerializer 

# from .models import Story



# @api_view(['GET'])
# def apiOverview(request):
#     api_urls = {
#         'List':'/story-list/',
#         'Detail View':'/story-detail/<str:pk>/',
#         'Create':'/story-create/',
#         'Update':'/story-update/<str:pk>/',
#         'Delete':'/story-delete/<str:pk>/',
#     }
#     return JsonResponse(api_urls)

# @api_view(['GET'])
# def storyList(request):
#     stories = Story.objects.all()
#     serializer = StorySerializer(stories,many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def storyDetail(request,pk):
#     stories = Story.objects.get(id=pk)
#     serializer = StorySerializer(stories,many=False)
#     return Response(serializer.data)

# @api_view(['POST'])
# def storyCreate(request):
#     serializer = StorySerializer(data=request.data)
    
#     if serializer.is_valid():
#         serializer.save()
        
#     return Response(serializer.data)

# @api_view(['POST'])
# def storyUpdate(request,pk):
#     story = Story.objects.get(id=pk)
#     serializer = StorySerializer(instance=story,data=request.data)
    
#     if serializer.is_valid():
#         serializer.save()
        
#     return Response(serializer.data)

# @api_view(['DELETE'])
# def storyDelete(request,pk):
#     story = Story.objects.get(id=pk)
#     story.delete()
    
        
#     return Response('item deleted successfully')

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Story
from .serializers import StorySerializer
from rest_framework import mixins



class StoryViewset(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.UpdateModelMixin,mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    '''
    API endpoint that allows one to view posts created   '''
    queryset = Story.objects.all()
    serializer_class = StorySerializer