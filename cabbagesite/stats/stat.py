from copy import deepcopy
from math import ceil

from stats.models import PlayersStats, FractionsStats
from reports.models import Report


class Stats:

    def __init__(self):
        self.reports = Report.objects.order_by('created_at')
        self.default_object = {'name': 'default', 'game_count': 0,
                               'victory': 0, 'rating': 100, 'description': ''}
        self.player_1_favorite = False
        self.players = {}
        self.fractions = {}

    def save(self):
        for report_index in range(len(self.reports)):
            report = self.reports[report_index]
            self._player_stat_count(report)
            self._fraction_stat_count(report)

        PlayersStats.objects.all().delete()
        FractionsStats.objects.all().delete()

        for player_name in self.players:
            player = self.players[player_name]
            PlayersStats.objects.create(
                name=player_name,
                games=player['game_count'],
                winrate=player['winrate'],
                rating=player['rating'],
                description=player['description']
            )

        for fraction_name in self.fractions:
            fraction = self.fractions[fraction_name]
            FractionsStats.objects.create(
                name=fraction_name,
                games=fraction['game_count'],
                winrate=fraction['winrate'],
                rating=fraction['rating'],
                description=fraction['description']
            )

    def _player_stat_count(self, report):
        if report.myself not in self.players:
            self.players[report.myself] = deepcopy(self.default_object)
            self.players[report.myself]['name'] = report.myself
        if report.opponent not in self.players:
            self.players[report.opponent] = deepcopy(self.default_object)
            self.players[report.opponent]['name'] = report.opponent

        myself, opponent = self.players[report.myself], \
            self.players[report.opponent]
        myself, opponent = self._game_count(myself, opponent)
        myself, opponent = self._player_rating_count(myself, opponent, report)
        myself, opponent = self._winrate_count(myself, opponent)

        self.players[report.myself] = myself
        self.players[report.opponent] = opponent

        return myself['rating']

    def _fraction_stat_count(self, report):
        if report.fraction_myself not in self.fractions:
            self.fractions[report.fraction_myself] = deepcopy(
                self.default_object)
            self.fractions[report.fraction_myself]['name'] = \
                report.fraction_myself
        if report.fraction_opponent not in self.fractions:
            self.fractions[report.fraction_opponent] = deepcopy(
                self.default_object
            )
            self.fractions[report.fraction_opponent]['name'] = \
                report.fraction_opponent

        myself, opponent = self.fractions[report.fraction_myself], \
            self.fractions[report.fraction_opponent]
        myself, opponent = self._game_count(myself, opponent)
        myself, opponent = self._fraction_rating_count(myself, opponent,
                                                       report)
        myself, opponent = self._winrate_count(myself, opponent)

        self.fractions[report.fraction_myself] = myself
        self.fractions[report.fraction_opponent] = opponent

    def _player_rating_count(self, myself, opponent, report):
        player_1 = myself['rating']
        player_2 = opponent['rating']

        if myself == opponent:
            rating_change = 0
        else:
            rating_differences = self._count_rating_differences(player_1,
                                                                player_2)
            player_1, player_2, rating_change = self._rating_accrual(
                report.victory, rating_differences, myself, opponent
            )

        self._add_player_description(myself, opponent, rating_change, report)

        myself['rating'] = player_1
        opponent['rating'] = player_2

        return myself, opponent

    def _fraction_rating_count(self, myself, opponent, report):
        rating_p1 = self.fractions[report.fraction_myself]['rating']
        rating_p2 = self.fractions[report.fraction_opponent]['rating']
        fraction_1 = myself['rating']
        fraction_2 = opponent['rating']

        if myself == opponent:
            rating_change = 0
        else:
            rating_differences_fractions = self._count_rating_differences(
                fraction_1, fraction_2)
            rating_differences_players = self._count_rating_differences(
                rating_p1, rating_p2)
            rating_differences = (rating_differences_fractions +
                                  rating_differences_players / 2)
            fraction_1, fraction_2, rating_change = self._rating_accrual(
                report.victory, rating_differences, myself, opponent)

        myself, opponent = self._add_fraction_description(myself,
                                                          opponent,
                                                          rating_change,
                                                          report)

        myself['rating'] = fraction_1
        opponent['rating'] = fraction_2

        return myself, opponent

    def _count_rating_differences(self, player_1, player_2):
        self.player_1_favorite = False

        if player_1 > 0 and player_2 > 0:
            if player_1 > player_2:
                self.player_1_favorite = True
                rating_differences = 1 - (player_1 - player_2) / player_1
            else:
                rating_differences = 1 - (player_2 - player_1) / player_2
        elif player_1 < 1 and player_2 > 0:
            rating_differences = 1 - (player_2 - 1) / player_2
        elif player_1 > 0 and player_2 < 1:
            self.player_1_favorite = True
            rating_differences = 1 - (player_1 - 1) / player_1
        else:
            rating_differences = 1

        return rating_differences

    def _rating_accrual(self, victory, rating_differences, myself, opponent):
        object_1 = myself['rating']
        object_2 = opponent['rating']

        if victory:
            if self.player_1_favorite:
                myself['victory'] += 1
                rating_change = ceil(10 * rating_differences)
                if rating_change > 20:
                    rating_change = 20
                object_1 += rating_change
                object_2 -= rating_change
            else:
                myself['victory'] += 1
                rating_change = ceil(10 / rating_differences)
                if rating_change > 20:
                    rating_change = 20
                object_1 += rating_change
                object_2 -= rating_change
        else:
            if self.player_1_favorite:
                opponent['victory'] += 1
                rating_change = ceil(10 / rating_differences)
                if rating_change > 20:
                    rating_change = 20
                object_1 -= rating_change
                object_2 += rating_change
            else:
                opponent['victory'] += 1
                rating_change = ceil(10 * rating_differences)
                if rating_change > 20:
                    rating_change = 20
                object_1 -= rating_change
                object_2 += rating_change

        if object_1 < 0:
            object_1 = 0
        if object_2 < 0:
            object_2 = 0

        return object_1, object_2, rating_change

    @staticmethod
    def _game_count(myself, opponent):
        myself['game_count'] += 1
        opponent['game_count'] += 1

        return myself, opponent

    @staticmethod
    def _winrate_count(myself, opponent):
        myself['winrate'] = int(myself['victory'] / myself['game_count'] * 100)
        opponent['winrate'] = int(opponent['victory'] / opponent['game_count']
                                  * 100)

        return myself, opponent

    @staticmethod
    def _add_player_description(myself, opponent, rating_change, report):

        if report.victory:
            myself_description = f'''
            <span class="victory myself">{myself["name"]}
            </span>({report.fraction_myself}) VS 
            <span class="defeat myself">{opponent["name"]}
            </span>({report.fraction_opponent})<br>
            Рейтинг {myself["rating"]}<span class="victory"> + 
            {rating_change}</span><br/>
            '''
            opponent_description = f'''
            <span class="defeat myself">{opponent["name"]}
            </span>({report.fraction_opponent}) VS 
            <span class="victory myself">{myself["name"]}
            </span>({report.fraction_myself})<br>
            Рейтинг {opponent["rating"]}<span class="defeat"> - 
            {rating_change}</span><br/>
            '''
        else:
            myself_description = f'''
            <span class="defeat myself">{myself["name"]}
            </span>({report.fraction_myself}) VS 
            <span class="victory myself">{opponent["name"]}
            </span>({report.fraction_opponent})<br>
            Рейтинг {myself["rating"]}<span class="defeat"> - 
            {rating_change}</span><br/>
            '''
            opponent_description = f'''
            <span class="victory myself">{opponent["name"]}
            </span>({report.fraction_opponent}) VS 
            <span class="defeat myself">{myself["name"]}
            </span>({report.fraction_myself})<br>
            Рейтинг {opponent["rating"]}<span class="victory"> + 
            {rating_change}</span><br/>
            '''

        myself['description'] += myself_description
        opponent['description'] += opponent_description

        return myself, opponent

    @staticmethod
    def _add_fraction_description(myself, opponent, rating_change, report):
        if report.victory:
            myself_description = f'''
            <span class="victory myself">{myself["name"]}
            </span>({report.myself}) VS 
            {opponent["name"]}({report.opponent})<br>
            Рейтинг {myself["rating"]}<span class="victory"> + 
            {rating_change}</span><br/>
            '''
            opponent_description = f'''
            <span class="defeat myself">{opponent["name"]}
            </span>({report.opponent}) VS 
            {myself["name"]}({report.myself})<br>
            Рейтинг {opponent["rating"]}<span class="defeat"> - 
            {rating_change}</span><br/>
            '''
        else:
            myself_description = f'''
            <span class="defeat myself">{myself["name"]}
            </span>({report.myself}) VS 
            {opponent["name"]}({report.opponent})<br>
            Рейтинг {myself["rating"]}<span class="defeat"> - 
            {rating_change}</span><br/>
            '''
            opponent_description = f'''
            <span class="victory myself">{opponent["name"]}
            </span>({report.opponent}) VS 
            {myself["name"]}({report.myself})<br>
            Рейтинг {opponent["rating"]}<span class="victory"> + 
            {rating_change}</span><br/>
            '''

        myself['description'] += myself_description
        opponent['description'] += opponent_description

        return myself, opponent
