from django.db import models
from django.contrib.auth.models import User



class BoardGame(models.Model):
    """A board game model"""
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    loaned = models.BooleanField()
    min_player_count = models.IntegerField()
    max_player_count = models.IntegerField()

    def __str__(self):
        """Return a string representation of the model"""
        return self.name


class LendedGames(models.Model):
    """A game log model"""
    game = models.ForeignKey(BoardGame, on_delete=models.CASCADE)
    date_lended = models.DateTimeField(auto_now_add=True)
    time_period = models.DateTimeField(auto_now=True)
    lender = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model"""
        return self.book.name + " - review"

'''
Board games
    -name
    -who added/owns
    -date added
    -description
    -loened bool
    -how many players
Lended games
    -board games
    -date loened
    -time period
    -who lended what
'''