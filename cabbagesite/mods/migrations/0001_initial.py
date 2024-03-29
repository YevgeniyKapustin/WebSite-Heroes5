# Generated by Django 4.0.5 on 2022-10-20 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('content', models.TextField(verbose_name='Содержание')),
                ('creators', models.TextField(verbose_name='Авторы')),
                ('photo', models.ImageField(upload_to='mods/', verbose_name='Изображение')),
                ('url', models.URLField(verbose_name='Cсылка')),
            ],
            options={
                'verbose_name': 'мод',
                'verbose_name_plural': 'Моды',
                'ordering': ['title'],
            },
        ),
    ]
