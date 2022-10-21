from django.db import models


class PlayersStats(models.Model):
    name = models.CharField(max_length=20, verbose_name='Игрок')
    games = models.BigIntegerField(verbose_name='Финалок игрока')
    winrate = models.BigIntegerField(verbose_name='Винрейт игрока')
    rating = models.BigIntegerField(verbose_name='Рейтинг игрока')
    description = models.TextField(verbose_name='Описание', default='История оказалась пуста ¯\\_(ツ)_/¯')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'винрейт игрока'
        verbose_name_plural = 'Винрейт игроков'
        ordering = ['-rating', '-games']


class FractionsStats(models.Model):
    name = models.CharField(max_length=20, verbose_name='Фракция')
    games = models.BigIntegerField(verbose_name='Финалок фракции')
    winrate = models.BigIntegerField(verbose_name='Винрейт фракции')
    rating = models.BigIntegerField(verbose_name='Рейтинг фракции')
    description = models.TextField(verbose_name='Описание', default='История оказалась пуста ¯\\_(ツ)_/¯')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'винрейт фракции'
        verbose_name_plural = 'Винрейт фракций'
        ordering = ['-rating', '-games']


class PlayersDescriptions(models.Model):
    player = models.ForeignKey('PlayersStats', on_delete=models.PROTECT, verbose_name='Игрок')
    description = models.TextField(verbose_name='Описание', default='История оказалась пуста ¯\\_(ツ)_/¯')
