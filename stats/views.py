from django.shortcuts import render
from stats.models import WinratePlayersStats, WinrateFractionsStats


def show_stat(request):
    context = {
        'WinratePlayersStats': WinratePlayersStats.objects.all(),
        'WinrateFractionsStats': WinrateFractionsStats.objects.all(),
        'TablePlayerCol1': 'Игроки',
        'TableFractionCol1': 'Фракция',
        'TableCol2': 'Финалок',
        'TableCol3': 'Винрейт',
        'Title': 'Главная'
    }
    return render(request, 'stats/stats.html', context)
