from django.urls import path
from .views import DonationViewset
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('', DonationViewset, basename='donation')
urlpatterns = router.urls