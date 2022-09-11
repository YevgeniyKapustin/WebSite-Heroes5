from django.shortcuts import render
from cabbagesite.settings import online_image, online_link


def show_online_game(request):
    context = {
        'title': 'Игра по сети',
        'link': online_link,
        'image': online_image
    }
    return render(request, 'online_game/online.html', context)
