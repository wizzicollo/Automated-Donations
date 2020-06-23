from django.urls import path
from .views import DonationViewset
from .views import StoryViewset
from .views import DonorViewset
from Dona import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('api/donation', DonationViewset, basename='donation')
router.register('api/story', StoryViewset, basename='story')
router.register('api/donor', DonorViewset, basename='donor')
urlpatterns = router.urls


from django.conf.urls import url 
from Dona import views 
from .views import CharityList
#..............

urlpatterns = [
    url(r'^api/charities/$', views.CharityList.as_view()),
    url(r'^api/charities/(?P<pk>[0-9]+)/$', views.CharityDetail.as_view()),
    url(r'^api/charities/approved/$', views.ApprovedCharities.as_view()),
]



