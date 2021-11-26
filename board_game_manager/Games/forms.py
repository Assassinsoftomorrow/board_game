from django import forms
from django.db import models
from django.forms import fields, widgets
from django import forms
from .models import BoardGame, LendedGames



class BoardGameForm(forms.ModelForm):
    class Meta:
        model = BoardGame
        fields = ['name', 'description', 'max_player_count', 'min_player_count']
        widgets = {'description': forms.Textarea(attrs={'cols': 80})}



'''
Form for adding game
    -name
    -description
    -how mane players
Form for lending games
    -name
    -time period
'''