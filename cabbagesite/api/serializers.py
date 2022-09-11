from rest_framework.serializers import ModelSerializer
from stats.models import WinratePlayersStats, WinrateFractionsStats


class PlayersStatSerializer(ModelSerializer):
    class Meta:
        model = WinratePlayersStats
        fields = ('name', 'games', 'winrate')


class FractionsStatSerializer(ModelSerializer):
    class Meta:
        model = WinrateFractionsStats
        fields = ('name', 'games', 'winrate')
