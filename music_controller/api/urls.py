from http.client import ImproperConnectionState
from django.urls import path
from .views import main

urlpatterns = [
    path('home', main),
]
