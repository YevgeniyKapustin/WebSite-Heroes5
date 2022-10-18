from copy import deepcopy
from math import ceil
from stats.models import PlayersStats, FractionsStats
from reports.models import Report


class Stats:

    def __init__(self):

        self.reports = Report.objects.all()
        self.default_object = {'game_count': 0, 'victory': 0, 'rating': 100}
        self.players = {}
        self.fractions = {}

    def save(self):

        for report_index in range(len(self.reports)):
            report = self.reports[report_index]
            self.__player_stat_count(report)
            self.__fraction_stat_count(report)

        PlayersStats.objects.all().delete()
        FractionsStats.objects.all().delete()

        for player_name in self.players:
            player = self.players[player_name]
            PlayersStats.objects.create(
                name=player_name,
                games=player['game_count'],
                winrate=player['winrate'],
                rating=player['rating']
            )

        for fraction_name in self.fractions:
            fraction = self.fractions[fraction_name]
            FractionsStats.objects.create(
                name=fraction_name,
                games=fraction['game_count'],
                winrate=fraction['winrate'],
                rating=fraction['rating']
            )

    def __player_stat_count(self, report):

        if report.myself not in self.players:
            self.players[report.myself] = deepcopy(self.default_object)
        if report.opponent not in self.players:
            self.players[report.opponent] = deepcopy(self.default_object)

        myself, opponent = self.players[report.myself], self.players[report.opponent]
        myself, opponent = self.__game_count(myself, opponent)
        myself, opponent = self.__rating_count(myself, opponent, report.victory)
        myself, opponent = self.__winrate_count(myself, opponent)

        self.players[report.myself] = myself
        self.players[report.opponent] = opponent

    def __fraction_stat_count(self, report):

        if report.fraction_myself not in self.fractions:
            self.fractions[report.fraction_myself] = deepcopy(self.default_object)
        if report.fraction_opponent not in self.fractions:
            self.fractions[report.fraction_opponent] = deepcopy(self.default_object)

        myself, opponent = self.fractions[report.fraction_myself], self.fractions[report.fraction_opponent]
        myself, opponent = self.__game_count(myself, opponent)
        myself, opponent = self.__rating_count(myself, opponent, report.victory)
        myself, opponent = self.__winrate_count(myself, opponent)

        self.fractions[report.fraction_myself] = myself
        self.fractions[report.fraction_opponent] = opponent

    @staticmethod
    def __game_count(myself, opponent):

        myself['game_count'] += 1
        opponent['game_count'] += 1

        return myself, opponent

    @staticmethod
    def __rating_count(myself, opponent, victory):

        player_1 = myself['rating']
        player_2 = opponent['rating']
        player_1_favorite = False

        if player_1 > 0 and player_2 > 0:
            if player_1 > player_2:
                player_1_favorite = True
                rating_different = 1 - (player_1 - player_2) / player_1
            else:
                rating_different = 1 - (player_2 - player_1) / player_2
        elif player_1 < 1 and player_2 > 0:
            rating_different = 1 - (player_2 - 1) / player_2
        elif player_1 > 0 and player_2 < 1:
            player_1_favorite = True
            rating_different = 1 - (player_1 - 1) / player_1
        else:
            rating_different = 1

        if rating_different > 2:
            rating_different = 2

        if victory:
            if player_1_favorite:
                myself['victory'] += 1
                player_1 += ceil(10 * rating_different)
                player_2 -= ceil(10 * rating_different)
            else:
                myself['victory'] += 1
                player_1 += ceil(10 / rating_different)
                player_2 -= ceil(10 / rating_different)
        else:
            if player_1_favorite:
                opponent['victory'] += 1
                player_1 -= ceil(10 / rating_different)
                player_2 += ceil(10 / rating_different)
            else:
                opponent['victory'] += 1
                player_1 -= ceil(10 * rating_different)
                player_2 += ceil(10 * rating_different)

        if player_1 < 0:
            player_1 = 0
        if player_2 < 0:
            player_2 = 0

        myself['rating'] = player_1
        opponent['rating'] = player_2

        return myself, opponent

    @staticmethod
    def __winrate_count(myself, opponent):

        myself['winrate'] = int(myself['victory'] / myself['game_count'] * 100)
        opponent['winrate'] = int(opponent['victory'] / opponent['game_count'] * 100)

        return myself, opponent
