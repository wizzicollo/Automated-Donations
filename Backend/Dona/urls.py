# from django.urls import path
# from . import views



# urlpatterns = [
#     path('', views.apiOverview,name="api-overview"),
#     path('story-list/',views.storyList,name="story-list"),
#     path('story-detail/<str:pk>/',views.storyDetail,name="story-detail"),
#     path('story-create/',views.storyCreate,name="story-create"),
#     path('story-update/<str:pk>/',views.storyUpdate,name="story-update"),
#     path('story-delete/<str:pk>/',views.storyDelete,name="story-delete")
 
# ]

from django.urls import path
from .views import StoryViewset
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('', StoryViewset, basename='story')
urlpatterns = router.urls