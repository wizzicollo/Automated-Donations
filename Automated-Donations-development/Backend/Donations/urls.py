from django.contrib import admin
from django.urls import path, include
from Dona import views

from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include 
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import include, path
from rest_framework import routers
from Dona import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('Dona.urls')),
    path('api/', include('rest_framework.urls', namespace='rest_framework'))
   
]

   








