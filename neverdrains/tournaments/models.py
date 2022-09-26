from django.db import models


class Tournament(models.Model):
    name = models.CharField(max_length=100)
    create_date = models.DateTimeField()

    def __str__(self) -> str:
        return self.name


class Division(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    score_1 = models.IntegerField()
    score_2 = models.IntegerField(null=True)
    score_3 = models.IntegerField(null=True)
    score_4 = models.IntegerField(null=True)
    score_5 = models.IntegerField(null=True)

    def __str__(self) -> str:
        return f"{self.tournament.name} - {self.description}"
