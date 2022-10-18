from rest_framework.serializers import ModelSerializer
from stats.models import PlayersStats, FractionsStats


class PlayersStatSerializer(ModelSerializer):
    class Meta:
        model = PlayersStats
        fields = ('name', 'games', 'winrate')


class FractionsStatSerializer(ModelSerializer):
    class Meta:
        model = FractionsStats
        fields = ('name', 'games', 'winrate')
