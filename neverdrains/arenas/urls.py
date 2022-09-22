from django.urls import path

from . import views

app_name = "arenas"

urlpatterns = [
    path("/", views.index, name="index"),
    path("<int:arena_id>/", views.arena_detail, name="detail"),
    # path("divisions/<int:division_id>/", views.divisions, name="divisions"),
]
