from django.db import models
from django.urls import reverse


class Home(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержание')
    photo = models.ImageField(upload_to='news/',  verbose_name='Изображение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']


class DownloadGame(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержание')
    photo = models.ImageField(upload_to='download_game/', verbose_name='Изображение')
    url = models.URLField(max_length=200, verbose_name='Cсылка')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'способ скачивание игры'
        verbose_name_plural = 'способы скачивания игры'
        ordering = ['-title']


class Mods(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержание')
    creators = models.TextField(verbose_name='Авторы')
    photo = models.ImageField(upload_to='mods/', verbose_name='Изображение')
    url = models.URLField(max_length=200, verbose_name='Cсылка')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'мод'
        verbose_name_plural = 'Моды'
        ordering = ['title']


class Maps(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержание')
    creators = models.TextField(verbose_name='Авторы')
    photo = models.ImageField(upload_to='maps', verbose_name='Изображение')
    url = models.URLField(max_length=200, verbose_name='Cсылка')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'карта'
        verbose_name_plural = 'Карты'
        ordering = ['title']


class Online(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержание')
    photo = models.ImageField(upload_to='online_game', verbose_name='Изображение')
    url = models.URLField(max_length=200, verbose_name='Cсылка')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'cпособ играть по сети'
        verbose_name_plural = 'Способы игры по сети'
        ordering = ['-title']


class Fractions(models.Model):
    title = models.CharField(max_length=20, db_index=True, verbose_name='Фракция')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'фракция'
        verbose_name_plural = 'Фракции'
        ordering = ['title']


class Report(models.Model):
    myself = models.CharField(max_length=15, verbose_name='Игрок')
    victory = models.BooleanField(default=True, verbose_name='Победа')
    opponent = models.CharField(max_length=15, verbose_name='Оппонент')
    fraction_myself = models.ForeignKey('fractions', on_delete=models.PROTECT, verbose_name='Фракция игрока',
                                        related_name='fraction_opponent')
    fraction_opponent = models.ForeignKey('fractions', on_delete=models.PROTECT, verbose_name='Фракция оппонента')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки')

    def __str__(self):
        return self.myself

    class Meta:
        verbose_name = 'отчёт'
        verbose_name_plural = 'Отчёты'
        ordering = ['myself']


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


class KateustaInfo(models.Model):
    pass


class Guides(models.Model):
    title = models.CharField(max_length=20, verbose_name='Заголовок')
    slug = models.SlugField(max_length=20, unique=True, db_index=True, verbose_name="Slug")
    content = models.TextField(verbose_name='Контент')

    def get_absolute_url(self):
        return reverse('guidedetail_view', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'руководство'
        verbose_name_plural = 'Руководства'
        ordering = ['title']
