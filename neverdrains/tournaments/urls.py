from django.urls import path

from . import views

app_name = "tournaments"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("divisions/<int:pk>/", views.DivisionView.as_view(), name="divisions"),
    path("divisions/<int:division_id>/entry", views.entry, name="entry"),
]
