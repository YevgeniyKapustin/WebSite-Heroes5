from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .forms import UserRegisterForm, UserLoginForm, ReportForm
from .models import Home, DownloadGame, Mods, Maps, Online, Report, WinratePlayersStats, WinrateFractionsStats


def report(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Отчёт отправлен')
            exemplar = HomeMain()
            exemplar.save_stats()
            return redirect('home')
        else:
            messages.error(request, 'Ошибка отправки отчёта')
    else:
        form = ReportForm()
    return render(request, 'main/report.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            x = HomeMain()
            x.save_stats()
            messages.success(request, 'Успешная регистрация')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'main/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'main/login.html', {'form': form})


class PlayersStatMain(ListView):
    model = WinratePlayersStats
    template_name = 'main/home_list.html'
    context_object_name = 'players_stats'


class FractionsStatMain(ListView):
    model = WinrateFractionsStats
    template_name = 'main/home_list.html'
    context_object_name = 'fractions_stats'


class HomeMain(ListView):
    model = Home

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ready_players = []
        self.ready_fractions = []
        self.reports = Report.objects.all()
        self.fractions_game_list = []

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['WinratePlayersStats'] = WinratePlayersStats.objects.all()
        context['WinrateFractionsStats'] = WinrateFractionsStats.objects.all()
        return context

    def save_stats(self):
        name_players, players_game_list, winrate_players = self.__return_data_players()
        name_fractions, fractions_game_list, winrate_fractions = self.__return_data_fractions()
        WinratePlayersStats.objects.all().delete()
        WinrateFractionsStats.objects.all().delete()
        for i in range(len(name_players)):
            WinratePlayersStats.objects.create(name=name_players[i],
                                               games=players_game_list[i],
                                               winrate=winrate_players[i])
        for i in range(len(name_fractions)):
            WinrateFractionsStats.objects.create(name=name_fractions[i],
                                                 games=fractions_game_list[i],
                                                 winrate=winrate_fractions[i])

    def __return_data_players(self):
        name_players_list, players_game_list, winrate_players_list = self.__create_players_winrate_data()
        name_players_list, winrate_players_list = self.__create_winrate_list(name_players_list, winrate_players_list)
        return name_players_list, players_game_list, winrate_players_list

    def __create_players_winrate_data(self):
        players_game_list, winrate_list = self.__create_players_winrate_list()
        return self.__create_players_list(), players_game_list, winrate_list

    def __create_players_list(self):
        name_list = []
        for report_item in self.reports:
            if report_item.myself not in name_list:
                name_list.append(report_item.myself)
            if report_item.opponent not in name_list:
                name_list.append(report_item.opponent)
        return name_list

    def __create_players_winrate_list(self):
        winrate_list = []
        players_game_list = []
        for index_player in range(len(self.reports)):
            if self.reports[index_player].myself not in self.ready_players:
                player = self.reports[index_player].myself
                winrate_list, players_game_list =\
                    self.__add_player_winrate_list(player, winrate_list, index_player, players_game_list)
            if self.reports[index_player].opponent not in self.ready_players:
                player = self.reports[index_player].opponent
                winrate_list, players_game_list = \
                    self.__add_player_winrate_list(player, winrate_list, index_player, players_game_list)
        return players_game_list, winrate_list

    def __add_player_winrate_list(self, player, winrate_list, index_player, players_game_list):
        self.ready_players.append(player)
        winrate, game_count = self.__players_winrate_calculation(index_player, player)
        winrate_list.append(winrate)
        players_game_list.append(game_count)
        return winrate_list, players_game_list

    def __players_winrate_calculation(self, index_player, player):
        game_count = 0
        victory_count = 0
        for index_game in range(len(self.reports)):
            if self.reports[index_game].myself == player:
                game_count += 1
                if self.reports[index_game].victory:
                    victory_count += 1
            elif self.reports[index_game].opponent == player:
                game_count += 1
                if not self.reports[index_game].victory:
                    victory_count += 1
        self.ready_players.append(self.reports[index_player].myself)
        return str(int(victory_count / game_count * 100)), game_count

    def __return_data_fractions(self):
        name_fraction_list, fractions_game_list, winrate_fraction_list = self.__create_fractions_winrate_data()
        name_fraction_list, winrate_fraction_list = \
            self.__create_winrate_list(name_fraction_list, winrate_fraction_list)
        return name_fraction_list, fractions_game_list, winrate_fraction_list

    def __create_fractions_winrate_data(self):
        winrate_list, fractions_game_list = self.__create_fractions_winrate_list()
        return self.__create_fractions_list(), fractions_game_list, winrate_list

    def __create_fractions_list(self):
        fractions_list = []
        for report_item in self.reports:
            if report_item.fraction_myself not in fractions_list:
                fractions_list.append(report_item.fraction_myself)
            if report_item.fraction_opponent not in fractions_list:
                fractions_list.append(report_item.fraction_opponent)
        return fractions_list

    def __create_fractions_winrate_list(self):
        winrate_list = []
        fractions_game_list = []
        for index_fraction in range(len(self.reports)):
            if self.reports[index_fraction].fraction_myself not in self.ready_fractions:
                fraction = self.reports[index_fraction].fraction_myself
                winrate_list, fractions_game_list = \
                    self.__add_fraction_winrate_list(fraction, winrate_list, index_fraction, fractions_game_list)
            if self.reports[index_fraction].fraction_opponent not in self.ready_fractions:
                fraction = self.reports[index_fraction].fraction_opponent
                winrate_list, fractions_game_list = \
                    self.__add_fraction_winrate_list(fraction, winrate_list, index_fraction, fractions_game_list)
        return winrate_list, fractions_game_list

    def __add_fraction_winrate_list(self, fraction, winrate_list, index_fraction, fractions_game_list):
        self.ready_fractions.append(fraction)
        winrate, game_count = self.__fractions_winrate_calculation(index_fraction, fraction)
        winrate_list.append(winrate)
        fractions_game_list.append(game_count)
        return winrate_list, fractions_game_list

    def __fractions_winrate_calculation(self, index_fraction, player):
        game_count = 0
        victory_count = 0
        for index_game in range(len(self.reports)):
            if self.reports[index_game].fraction_myself == player:
                game_count += 1
                if self.reports[index_game].victory and \
                        self.reports[index_game].fraction_myself != self.reports[index_game].fraction_opponent:
                    victory_count += 1
            if self.reports[index_game].fraction_opponent == player:
                game_count += 1
                if not self.reports[index_game].victory and \
                        self.reports[index_game].fraction_myself != self.reports[index_game].fraction_opponent:
                    victory_count += 1
        self.ready_fractions.append(self.reports[index_fraction].fraction_myself)
        return int(victory_count / game_count * 100), game_count

    @staticmethod
    def __create_winrate_list(name_list, winrate_list):
        objects_name = []
        objects_winrate = []
        for index in range(len(name_list)):
            objects_name.append('{}'.format(name_list[index]))
        for index in range(len(winrate_list)):
            objects_winrate.append('{}%'.format(winrate_list[index]))
        return objects_name, objects_winrate


class GameMain(ListView):
    model = DownloadGame


class ModsMain(ListView):
    model = Mods


class MapsMain(ListView):
    model = Maps


class OnlineMain(ListView):
    model = Online
