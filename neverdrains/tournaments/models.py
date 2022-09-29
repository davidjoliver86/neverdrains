from django.db import models


class Tournament(models.Model):
    name = models.CharField(max_length=100)
    timestamp = models.DateTimeField()

    def __str__(self) -> str:
        return self.name


class Division(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)

    # Number of arenas that count toward a players' meaningful tournament score.
    # If null, assume all arenas count.
    arenas_counted = models.IntegerField(null=True)

    # The score_1-5 fields represent how to handle the top 5 positions.
    # Only score_1 - the max score - is required.
    # If any score_x field is null, all the other fields after it should be null too.
    # Score progression will go down one point for every rank after the lowest of these values.

    score_1 = models.IntegerField()
    score_2 = models.IntegerField(null=True)
    score_3 = models.IntegerField(null=True)
    score_4 = models.IntegerField(null=True)
    score_5 = models.IntegerField(null=True)

    def __str__(self) -> str:
        return f"{self.tournament.name} - {self.description}"

    def get_ranks(self):
        ranks = [self.score_1]
        for attr in range(2, 6):
            attr_name = f"score_{attr}"
            value = getattr(self, attr_name)
            if value is None:
                return ranks
            ranks.append(value)
        return ranks
