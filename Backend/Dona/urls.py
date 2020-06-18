from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url 
from Dona import views 
#..............

urlpatterns=[
    url(r'^api/charities$', views.charities_list),
    url(r'^api/charities/(?P<pk>[0-9]+)$', views.charity_detail),
    url(r'^api/charities/published$', views.charities_list_published)
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)