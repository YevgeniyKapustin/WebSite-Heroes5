from django.db import models


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
        ordering = ['-created_at']
