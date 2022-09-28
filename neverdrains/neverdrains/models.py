from django.db import models

from tournaments.models import Division

# Create your models here.


class Arena(models.Model):
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=20, default=None)

    def __str__(self) -> str:
        return self.name


class ArenaInBank(models.Model):
    """
    Machines are assigned to a division of a tournament. All tournaments should have at
    least one division, even if it is just "main".

    A collection of ArenaInBank instances should constitute a bank in a tournament.
    """

    arena = models.ForeignKey(Arena, on_delete=models.CASCADE)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.arena.name} - {self.division}"

