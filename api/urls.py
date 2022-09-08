from django.urls import path
from api.views import PlayersStatAPIView, FractionsStatAPIView

urlpatterns = [
    path('players_winrate/', PlayersStatAPIView.as_view(), name='players_winrate'),
    path('fractions_winrate/', FractionsStatAPIView.as_view(), name='fractions_winrate'),
]
