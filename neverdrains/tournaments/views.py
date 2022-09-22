from django.shortcuts import render, get_object_or_404
from . import models


def index(request):
    tournaments = models.Tournament.objects.all()
    context = {"tournaments": tournaments}
    return render(request, "tournaments/index.html", context)


def tournament_detail(request, tournament_id):
    tournament = get_object_or_404(models.Tournament, pk=tournament_id)
    return render(request, "tournaments/detail.html", {"tournament": tournament})


def divisions(request, division_id):
    division = get_object_or_404(models.Division, pk=division_id)
    return render(request, "tournaments/division.html", {"division": division})
