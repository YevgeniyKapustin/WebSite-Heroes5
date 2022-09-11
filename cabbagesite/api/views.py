from rest_framework.generics import ListAPIView
from api.serializers import PlayersStatSerializer, FractionsStatSerializer
from stats.models import WinratePlayersStats, WinrateFractionsStats


class PlayersStatAPIView(ListAPIView):
    queryset = WinratePlayersStats.objects.all()
    serializer_class = PlayersStatSerializer


class FractionsStatAPIView(ListAPIView):
    queryset = WinrateFractionsStats.objects.all()
    serializer_class = FractionsStatSerializer
