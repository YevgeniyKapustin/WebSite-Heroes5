# Generated by Django 4.0.5 on 2022-10-20 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fractions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=20, verbose_name='Фракция')),
            ],
            options={
                'verbose_name': 'фракция',
                'verbose_name_plural': 'Фракции',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('myself', models.CharField(max_length=15, verbose_name='Игрок')),
                ('victory', models.BooleanField(default=True, verbose_name='Победа')),
                ('opponent', models.CharField(max_length=15, verbose_name='Оппонент')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки')),
                ('fraction_myself', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='fraction_opponent', to='reports.fractions', verbose_name='Фракция игрока')),
                ('fraction_opponent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reports.fractions', verbose_name='Фракция оппонента')),
            ],
            options={
                'verbose_name': 'отчёт',
                'verbose_name_plural': 'Отчёты',
                'ordering': ['myself'],
            },
        ),
    ]
