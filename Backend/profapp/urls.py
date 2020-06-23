from django.urls import path

from .views import ProfileRetrieveAPIView

app_name = 'profapp'
urlpatterns = [
    path('profiles/<str:username>', ProfileRetrieveAPIView.as_view()),
]