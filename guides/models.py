from django.db import models
from django.urls import reverse


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
