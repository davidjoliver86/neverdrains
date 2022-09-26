from django.http import HttpResponse
from django.views.generic import DetailView
from . import models

from typing import Dict, Any


def index(request):
    return HttpResponse("This is the arenas index.")


def arena_detail(request, arena_id):
    return HttpResponse(f"This is arena ID {arena_id}.")


class AABDetailView(DetailView):
    model = models.ArenaInBank
    template_name = "arenas/arena_in_bank.html"
    context_object_name = "aab"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        return ctx
