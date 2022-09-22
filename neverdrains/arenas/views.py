from django.shortcuts import render, get_object_or_404
from . import models


def index(request):
    arenas = models.Arena.objects.all()
    context = {"arenas": arenas}
    return render(request, "arenas/index.html", context)


def arena_detail(request, arena_id):
    arena = get_object_or_404(models.Arena, pk=arena_id)
    return render(request, "arenas/detail.html", {"arena": arena})
