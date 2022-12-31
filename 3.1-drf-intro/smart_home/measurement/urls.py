from django.urls import path
from .views import CreateAPIView, ListCreateAPIView, RetrieveUpdateAPIView

urlpatterns = [
    path('sensors/', CreateAPIView.as_view()),
    path('sensors/<pk>/', RetrieveUpdateAPIView.as_view()),
    path('measurements/', ListCreateAPIView.as_view()),
]
