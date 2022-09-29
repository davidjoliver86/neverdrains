from typing import Dict, Any
from operator import itemgetter

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
        """
        Returns all entries for a machine in the bank, appending the rank and score to each entry.

        This is ultimately responsible for computing a player's "tournament score" for a machine in
        a given divisions' bank. Use this as a starting point before diving into further
        aggregations.

        On the ArenaInBank details page, this is used straight as-is.
        On the RegisteredPlayer details page, this is used for the score summary.
        On the Division details page, these are factored into all players' scores.
        """
        entries = cls.objects.filter(arena=aab_id, void=False).order_by("-score")
        if not entries:
            return entries
        results = {}
        for index, entry in enumerate(entries):
            # We already retrieve Entry records in descending score order. This is a lower score
            # than the player's last attempt, so disregard this entry.
            if entry.player in results:
                continue

            record = {"score": entry.score, "timestamp": entry.timestamp, "player": entry.player}
            results[entry.player] = record

        # Apply rankings
        ranks = entries[0].arena.division.get_ranks()
        while ranks[-1] > 0:
            ranks.append(ranks[-1] - 1)
        results = sorted(results.values(), key=itemgetter("score"), reverse=True)
        for index, entry in enumerate(results):
            try:
                entry["rank_score"] = ranks[index]
            except IndexError:
                entry["rank_score"] = 0
        return results
