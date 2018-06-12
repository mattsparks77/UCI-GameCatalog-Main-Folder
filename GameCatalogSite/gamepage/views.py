from django.shortcuts import render

def bioshock(request):
    return render(request, 'gamepage/bioshock.html')

def tetris(request):
    return render(request, 'gamepage/tetris.html')

def sonic_adventure(request):
    return render(request, 'gamepage/sonic_adventure.html')
