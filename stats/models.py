from django.db import models


class WinratePlayersStats(models.Model):
    name = models.CharField(max_length=20, verbose_name='Игрок')
    games = models.BigIntegerField(verbose_name='Финалок игрока')
    winrate = models.BigIntegerField(verbose_name='Винрейт игрока')

    class Meta:
        verbose_name = 'винрейт игрока'
        verbose_name_plural = 'Винрейт игроков'
        ordering = ['-winrate', '-games']


class WinrateFractionsStats(models.Model):
    name = models.CharField(max_length=20, verbose_name='Фракция')
    games = models.BigIntegerField(verbose_name='Финалок фракции')
    winrate = models.BigIntegerField(verbose_name='Винрейт фракции')

    class Meta:
        verbose_name = 'винрейт фракции'
        verbose_name_plural = 'Винрейт фракций'
        ordering = ['-winrate', '-games']

