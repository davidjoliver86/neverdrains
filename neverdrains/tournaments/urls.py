from django.urls import path

from . import views

app_name = "tournaments"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:tournament_id>/", views.tournament_detail, name="detail"),
    path("divisions/<int:division_id>/", views.divisions, name="divisions"),
]
