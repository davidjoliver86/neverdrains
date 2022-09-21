from __future__ import division
from django.db import models

# Create your models here.
class Tournament(models.Model):
    name = models.CharField(max_length=100)
    create_date = models.DateTimeField()

    def __str__(self) -> str:
        return f"Tournament: {self.name}"


class Division(models.Model):
    name = models.CharField(max_length=100)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Division {self.name} of Tournament {self.tournament.name}"


class Arena(models.Model):
    name = models.CharField(max_length=100)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)

    def __str__(self) -> str:
        # pylint: disable=no-member
        return f"Arena: {self.name} of {self.division.tournament.name}, {self.division.name}"
