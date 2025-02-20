from django.urls import path
from . import main

urlpatterns = [
    path('',main.weather_view,name='Weather')
]
