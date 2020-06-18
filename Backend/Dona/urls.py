from django.conf.urls import url 
from Dona import views 
#..............

urlpatterns=[
    url(r'^api/charities$', views.charities_list),
    url(r'^api/charities/(?P<pk>[0-9]+)$', views.charity_detail),
    url(r'^api/charities/published$', views.approved_charities_list)
]
