# Generated by Django 2.1.1 on 2018-09-05 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('importdata', '0009_igdbgame_time_to_beat'),
    ]

    operations = [
        migrations.AddField(
            model_name='igdbgame',
            name='genres',
            field=models.ManyToManyField(to='importdata.Genre'),
        ),
    ]