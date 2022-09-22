# Generated by Django 4.1.1 on 2022-09-22 01:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("arenas", "0001_initial"),
        ("players", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Entry",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("score", models.BigIntegerField()),
                ("void", models.BooleanField(default=False)),
                ("timestamp", models.DateTimeField()),
                (
                    "arena",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="arenas.arenainbank"
                    ),
                ),
                (
                    "player",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="players.registeredplayer"
                    ),
                ),
            ],
        ),
    ]
