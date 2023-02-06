from django.urls import path

from online_game.views import show_online_game

urlpatterns = [
    path('', show_online_game, name='online_game')
]
