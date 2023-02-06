from django.shortcuts import render

from maps.models import Maps


def maps_single(request):
    context = {
        'title': 'Одиночные карты',
        'Button': 'Скачать',
        'Prefix': 'Авторство: ',
        'maps': Maps.objects.filter(type='single')
    }
    return render(request, 'maps/maps_single.html', context)


def maps_multiplayer(request):
    context = {
        'title': 'Мультиплеерные карты',
        'Button': 'Скачать',
        'Prefix': 'Авторство: ',
        'maps': Maps.objects.filter(type='multiplayer')
    }
    return render(request, 'maps/maps_multiplayer.html', context)


def maps_install(request):
    return render(request, 'maps/maps_install.html')
