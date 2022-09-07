# Generated by Django 4.0.5 on 2022-09-07 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WinrateFractionsStats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Фракция')),
                ('games', models.BigIntegerField(verbose_name='Финалок фракции')),
                ('winrate', models.BigIntegerField(verbose_name='Винрейт фракции')),
            ],
            options={
                'verbose_name': 'винрейт фракции',
                'verbose_name_plural': 'Винрейт фракций',
                'ordering': ['-winrate', '-games'],
            },
        ),
        migrations.CreateModel(
            name='WinratePlayersStats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Игрок')),
                ('games', models.BigIntegerField(verbose_name='Финалок игрока')),
                ('winrate', models.BigIntegerField(verbose_name='Винрейт игрока')),
            ],
            options={
                'verbose_name': 'винрейт игрока',
                'verbose_name_plural': 'Винрейт игроков',
                'ordering': ['-winrate', '-games'],
            },
        ),
    ]