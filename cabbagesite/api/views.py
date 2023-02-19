from rest_framework.generics import ListAPIView

from api.serializers import PlayersStatSerializer, FractionsStatSerializer
from stats.models import PlayersStats, FractionsStats


class PlayersStatAPIView(ListAPIView):
    queryset = PlayersStats.objects.all()
    serializer_class = PlayersStatSerializer


class FractionsStatAPIView(ListAPIView):
    queryset = FractionsStats.objects.all()
    serializer_class = FractionsStatSerializer
