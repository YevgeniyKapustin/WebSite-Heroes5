# Generated by Django 4.0.5 on 2022-10-20 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guides',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='Заголовок')),
                ('slug', models.SlugField(max_length=20, unique=True, verbose_name='Slug')),
                ('content', models.TextField(verbose_name='Контент')),
            ],
            options={
                'verbose_name': 'руководство',
                'verbose_name_plural': 'Руководства',
                'ordering': ['title'],
            },
        ),
    ]
