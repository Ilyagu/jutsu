# Generated by Django 3.1.5 on 2021-01-12 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jutsu', '0007_auto_20210110_0433'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genre',
            name='animes',
        ),
        migrations.AddField(
            model_name='anime',
            name='genres',
            field=models.ManyToManyField(through='jutsu.Anime_Genre', to='jutsu.Genre'),
        ),
    ]
