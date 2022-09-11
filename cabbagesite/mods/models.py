from django.db import models


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
