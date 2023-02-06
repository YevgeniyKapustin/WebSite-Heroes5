from django.urls import path

from api.views import PlayersStatAPIView, FractionsStatAPIView

urlpatterns = [
    path('players_stats/', PlayersStatAPIView.as_view(), name='players_stats'),
    path('fractions_stats/', FractionsStatAPIView.as_view(),
         name='fractions_winrate'),
]
