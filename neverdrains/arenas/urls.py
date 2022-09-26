from django.urls import path

from . import views

app_name = "arenas"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:arena_id>/", views.arena_detail, name="detail"),
    path("inbank/<int:pk>", views.AABDetailView.as_view(), name="arena_in_bank_detail"),
]
