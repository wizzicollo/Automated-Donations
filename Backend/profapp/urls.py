from django.urls import path

from .views import ProfileRetrieveAPIView

app_name = 'profapp'
urlpatterns = [
    path('profiles/<int:pk>', ProfileRetrieveAPIView.as_view()),
]