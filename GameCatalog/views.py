from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the GameCatalog index.\n WE ARE THE CREATORS WE SLAY THE GAMES: Plus Denenburg \n Matt Sparks \n Daniel Williams \n Whitney Tran \n David Wong")
