from django.db import models


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
