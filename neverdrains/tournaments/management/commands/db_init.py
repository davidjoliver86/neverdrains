import datetime
import random
from pytz import timezone

from django.conf import settings
from django.db import transaction
from django.core.management.base import BaseCommand

from tournaments import models as tm_models
from arenas import models as ar_models
from entries import models as en_models
from players import models as pl_models


class Command(BaseCommand):
    help = "Initializes a fresh database with fake data."

    @transaction.atomic
    def handle(self, *args, **kwargs):
        now = datetime.datetime.now()

        # Create a tournament
        tournament = tm_models.Tournament(name="INDISC 2023", timestamp=now)
        tournament.save()
        print(f"Saved {tournament}")

        # Create divisions
        the_open = tm_models.Division(
            name="open",
            tournament=tournament,
            description="The Open",
            arenas_counted=6,
            score_1=200,
            score_2=190,
            score_3=185,
            score_4=180,
        )
        the_open.save()
        print(f"Saved {the_open}")

        classics = tm_models.Division(
            name="classics",
            tournament=tournament,
            description="Classics1",
            arenas_counted=4,
            score_1=200,
            score_2=190,
            score_3=185,
            score_4=180,
        )
        classics.save()
        print(f"Saved {classics}")

        # Create Arenas
        for name, abbrev in (
            ("Attack from Mars", "AFM"),
            ("Black Rose", "BR"),
            ("Centaur", "CTR"),
            ("Demolition Man", "DM"),
            ("Elvira's House of Horrors", "EHOH"),
            ("Family Guy", "FG"),
            ("Godzilla", "GZ"),
            ("Harlem Globetrotters", "HG"),
            ("Iron Maiden", "IMDN"),
            ("Johnny Mnenomic", "JM"),
        ):
            arena = ar_models.Arena(name=name, abbreviation=abbrev)
            arena.save()
            print(f"Saved {arena}")
            aab = ar_models.ArenaInBank(arena=arena, division=the_open)
            aab.save()
            print(f"Saved {aab}")

        for name, abbrev in (
            ("Abra Ca Dabra", "ACD"),
            ("Black Jack", "BJ"),
            ("Centigrade 37", "C37"),
            ("Dragonfist", "DF"),
            ("Eight Ball Deluxe", "EBD"),
            ("Firepower", "FP"),
            ("Galaxy", "GXY"),
            ("Hit The Deck", "HTD"),
            ("Ice Fever", "IF"),
            ("Joker Poker", "JP"),
        ):
            arena = ar_models.Arena(name=name, abbreviation=abbrev)
            arena.save()
            print(f"Saved {arena}")
            aab = ar_models.ArenaInBank(arena=arena, division=classics)
            aab.save()
            print(f"Saved {aab}")

        # Players
        for first, last, pref, ifpa in (
            ("David", "Oliver", "DAVIDO", 36206),
            ("Keith", "Elwin", "The GOAT", 1),
            ("Raymond", "Davidson", "RayDay", 2576),
            ("Escher", "Lefkoff", None, 1605),
        ):
            player = pl_models.Player(
                first_name=first, last_name=last, preferred_name=pref, ifpa_id=ifpa
            )
            player.save()
            print(f"Saved {player}")
            rp = pl_models.RegisteredPlayer(player=player, tournament=tournament)
            rp.save()
            print(f"Saved {rp}")

        # Scores
        for division in the_open, classics:
            for arena in ar_models.ArenaInBank.objects.filter(division=division):
                tournament = division.tournament
                for player in pl_models.RegisteredPlayer.objects.filter(tournament=tournament):
                    for _ in range(3):
                        if division is the_open:
                            score = random.randint(0, 9_000_000) + 1_000_000
                        else:
                            score = random.randint(0, 990_000) + 10_000
                        aware = timezone(settings.TIME_ZONE).localize(now)
                        entry = en_models.Entry(
                            arena=arena,
                            player=player,
                            score=score,
                            timestamp=aware,
                        )
                        entry.save()
