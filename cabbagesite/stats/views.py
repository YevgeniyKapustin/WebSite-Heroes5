from django.shortcuts import render, redirect
from stats.models import PlayersStats, FractionsStats


def show_stat(request):
    context = {
        'WinratePlayersStats': PlayersStats.objects.all(),
        'WinrateFractionsStats': FractionsStats.objects.all(),
        'TablePlayerCol1': 'Игроки',
        'TableFractionCol1': 'Фракция',
        'TableCol2': 'Финалок',
        'TableCol3': 'Винрейт',
        'TableCol4': 'Рейтинг',
        'Title': 'Главная'
    }
    return render(request, 'stats/stats.html', context)


def redirect_to_stat(request):
    return redirect('stats')
