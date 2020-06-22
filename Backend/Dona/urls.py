from django.conf.urls import url 
from Dona import views 
from .views import CharityList
#..............

urlpatterns = [
    url(r'^api/charities/$', views.CharityList.as_view()),
    url(r'^api/charities/(?P<pk>[0-9]+)/$', views.CharityDetail.as_view()),
    url(r'^api/charities/approved/$', views.ApprovedCharities.as_view()),
]
