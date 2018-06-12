from django.urls import path
from . import views

urlpatterns = [
    path('sonic_adventure/', views.sonic_adventure, name='sonic_adventure'),
    path('tetris/', views.tetris, name='tetris'),
    path('bioshock/', views.bioshock, name='bioshock'),
]
