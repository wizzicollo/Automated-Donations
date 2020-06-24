from django.urls import path
from .views import DonationViewset
from .views import StoryViewset
from .views import DonorViewset
from Dona import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('donation', DonationViewset, basename='donation')
router.register('story', StoryViewset, basename='story')
router.register('donor', DonorViewset, basename='donor')
router.register('charity',views.CharityViewSet, basename='charity')
urlpatterns = router.urls






