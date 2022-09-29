from collections import namedtuple

from django.db import models

from tournaments.models import Tournament


class Player(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    preferred_name = models.CharField(max_length=100, null=True)
    ifpa_id = models.IntegerField(null=True)

    @property
    def name(self):
        if self.preferred_name:
            return self.preferred_name
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"Player: {self.name}"


class RegisteredPlayer(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)

    def __str__(self):
        return f"Player {self.player.name} registered in {self.tournament.name}"


PlayerRanking = namedtuple("PlayerRanking", ["player", "score"])
