from django.urls import path
from . import views

urlpatterns = [
    path('bioshock/', views.bioshock, name='bioshock'),
    path('tetris/', views.tetris, name='tetris'),
    path('sonic_adventure/', views.sonic_adventure, name='sonic_adventure'),
]
