from django.urls import path

from . import views

app_name = "entries"

urlpatterns = [
    path("/", views.index, name="index"),
    path("<int:entry_id>/", views.entry_detail, name="detail"),
]
