from django.urls import path
from .views import DonorViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', DonorViewset, basename='donor')
urlpatterns = router.urls