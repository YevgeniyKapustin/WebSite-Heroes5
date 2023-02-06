from django.shortcuts import render

from cabbagesite.settings import game_link, game_image


def show_download_game(request):
    context = {
        'title': 'Скачать герои5',
        'link': game_link,
        'image': game_image
    }
    return render(request, 'download_game/game.html', context)
