# Generated by Django 3.2.9 on 2021-11-26 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Games', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='boardgame',
            name='game_image',
            field=models.ImageField(default='default.jpg', upload_to='images/'),
        ),
    ]