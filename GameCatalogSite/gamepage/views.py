from django.shortcuts import render

def sonic_adventure(request):
    return render(request, 'gamepage/sonic_adventure.html')

def tetris(request):
    return render(request, 'gamepage/tetris.html')

def bioshock(request):
    return render(request, 'gamepage/bioshock.html')
