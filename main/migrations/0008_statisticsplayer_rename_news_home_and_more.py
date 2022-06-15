# Generated by Django 4.0.4 on 2022-06-11 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_fraction_alter_downloadgame_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatisticsPlayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player', models.CharField(max_length=20, verbose_name='Игрок')),
                ('winrate', models.CharField(max_length=3, verbose_name='винрейт')),
            ],
            options={
                'verbose_name': 'Статистика игрока',
                'verbose_name_plural': 'Статистика игроков',
                'ordering': ['winrate'],
            },
        ),
        migrations.RenameModel(
            old_name='News',
            new_name='Home',
        ),
        migrations.AlterModelOptions(
            name='fraction',
            options={'ordering': ['title'], 'verbose_name': 'фракция', 'verbose_name_plural': 'Фракции'},
        ),
        migrations.AlterField(
            model_name='report',
            name='victory',
            field=models.BooleanField(verbose_name='Победа'),
        ),
        migrations.CreateModel(
            name='FractionPlayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('winrate', models.CharField(max_length=3, verbose_name='винрейт')),
                ('fraction', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.fraction', verbose_name='Фракция')),
            ],
            options={
                'verbose_name': 'Статистика фракции',
                'verbose_name_plural': 'Статистика фракций',
                'ordering': ['winrate'],
            },
        ),
    ]
