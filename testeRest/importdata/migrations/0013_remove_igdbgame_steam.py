# Generated by Django 2.1.1 on 2018-09-06 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('importdata', '0012_igdbgame_steam'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='igdbgame',
            name='steam',
        ),
    ]