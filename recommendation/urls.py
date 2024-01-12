from django.urls import path
from .views import get_vaccines
urlpatterns = [
    path('', get_vaccines, name="vaccines"),
]
   
