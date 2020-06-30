from django.urls import path
from .views import StoryViewset
from Dona import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('story', StoryViewset, basename='story')
router.register('charity',views.CharityViewSet, basename='charity')

urlpatterns = router.urls






