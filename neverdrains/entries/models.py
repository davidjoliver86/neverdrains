from django.db import models
from arenas.models import ArenaInBank
from players.models import RegisteredPlayer


# Create your models here.


class Entry(models.Model):
    player = models.ForeignKey(RegisteredPlayer, on_delete=models.CASCADE)
    arena = models.ForeignKey(ArenaInBank, on_delete=models.CASCADE)
    score = models.BigIntegerField()
    void = models.BooleanField(default=False)
    timestamp = models.DateTimeField()

    def __str__(self) -> str:
        return "Player {self.player.name}: {self.score} on {self.arena.arena.name}"
