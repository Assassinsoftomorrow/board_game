# Generated by Django 3.2.9 on 2021-12-02 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Games', '0002_boardgame_game_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lendedgames',
            name='time_period',
            field=models.DateTimeField(),
        ),
    ]
