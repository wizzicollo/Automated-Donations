from django.urls import path, include

from .views import ProfileRetrieveAPIView

app_name = 'Dona'
urlpatterns = [
    path('profiles/<str:username>', ProfileRetrieveAPIView.as_view()),
]

