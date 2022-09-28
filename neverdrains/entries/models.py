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
        return f"Player {self.player.player.name}: {self.score} on {self.arena.arena.name}"

    @classmethod
    def arena_in_bank_rankings(cls, aab_id: int):
        entries = cls.objects.filter(arena=aab_id, void=False).order_by("-score")
        if not entries:
            return entries
        all_ranks = (
            entries[0].arena.division.score_1,
            entries[0].arena.division.score_2,
            entries[0].arena.division.score_3,
            entries[0].arena.division.score_4,
            entries[0].arena.division.score_5,
        )
        ranks = tuple(filter(None, all_ranks))
        for index, entry in enumerate(entries):
            entry.rank = index + 1
            try:
                entry.rank_score = ranks[index]
            except IndexError:
                entry.rank_score = max(ranks[-1] - index + len(ranks) - 1, 0)
        return entries
