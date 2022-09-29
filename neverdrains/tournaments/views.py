import re
import datetime
from typing import Dict, Any
from operator import attrgetter

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views import generic
from django.urls import reverse

from . import models
from players.models import RegisteredPlayer, PlayerRanking
from arenas.models import ArenaInBank
from entries.models import Entry
from entries.exceptions import ScoreValidationException


class IndexView(generic.ListView):
    model = models.Tournament
    template_name = "tournaments/index.html"


class DetailView(generic.DetailView):
    model = models.Tournament
    template_name = "tournaments/detail.html"


class DivisionView(generic.DetailView):
    model = models.Division
    template_name = "tournaments/division.html"

    def _build_rankings(self):
        arenas = get_list_or_404(ArenaInBank, division_id=self.kwargs["pk"])
        player_data = {}
        for arena in arenas:
            entries = Entry.arena_in_bank_rankings(arena.pk)
            for entry in entries:
                entry["arena"] = arena
                player = entry["player"]
                player_data[player] = player_data.get(player, []) + [entry]

        # Build rankings from aggregated player data. Sort by players' top rank scores,
        # taking the cutoff as necessary.

        rankings = []
        for player, scores in player_data.items():
            best_scores = sorted((score["rank_score"] for score in scores), reverse=True)
            if cutoff := self.object.arenas_counted:
                best_scores = best_scores[:cutoff]
            rankings.append(PlayerRanking(player=player.player.name, score=sum(best_scores)))
        rankings.sort(key=attrgetter("score"), reverse=True)
        return rankings

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        ctx["rankings"] = self._build_rankings()
        return ctx


def entry(request, division_id):
    division = get_object_or_404(models.Division, pk=division_id)
    players = get_list_or_404(RegisteredPlayer, tournament=division.tournament)
    arenas = get_list_or_404(ArenaInBank, division_id=division_id)
    context = {"players": players, "arenas": arenas, "division": division}
    if request.method == "POST":
        # Validate that the player and arena from the POST request exist
        player = get_object_or_404(RegisteredPlayer, pk=request.POST["player"])
        arena = get_object_or_404(ArenaInBank, pk=request.POST["arena"])

        # Validate score
        score = request.POST["score"]
        if not re.match(r"^[0-9]+", score):
            raise ScoreValidationException("Invalid format for score")

        # All good, create new model
        entry = Entry()
        entry.arena = arena
        entry.player = player
        entry.score = int(score)
        if request.POST.get("void"):
            entry.void = True
        entry.timestamp = datetime.datetime.now()
        entry.save()
        return HttpResponseRedirect(reverse("tournaments:divisions", args=(division_id,)))
    return render(request, "tournaments/entry.html", context)
