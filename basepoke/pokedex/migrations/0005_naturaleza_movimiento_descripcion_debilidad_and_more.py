# Generated by Django 5.2 on 2025-05-20 18:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pokedex", "0004_delete_pokeball"),
    ]

    operations = [
        migrations.CreateModel(
            name="Naturaleza",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=50, unique=True)),
                (
                    "aumenta",
                    models.CharField(
                        choices=[
                            ("Ataque", "Ataque"),
                            ("Defensa", "Defensa"),
                            ("Ataque_Especial", "Ataque Especial"),
                            ("Defensa_Especial", "Defensa Especial"),
                            ("Velocidad", "Velocidad"),
                            ("Ninguna", "Ninguna"),
                        ],
                        default="Ninguna",
                        max_length=20,
                    ),
                ),
                (
                    "disminuye",
                    models.CharField(
                        choices=[
                            ("Ataque", "Ataque"),
                            ("Defensa", "Defensa"),
                            ("Ataque_Especial", "Ataque Especial"),
                            ("Defensa_Especial", "Defensa Especial"),
                            ("Velocidad", "Velocidad"),
                            ("Ninguna", "Ninguna"),
                        ],
                        default="Ninguna",
                        max_length=20,
                    ),
                ),
                ("descripcion", models.TextField(blank=True, null=True)),
            ],
            options={
                "verbose_name": "Naturaleza",
                "verbose_name_plural": "Naturalezas",
            },
        ),
        migrations.AddField(
            model_name="movimiento",
            name="Descripcion",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name="Debilidad",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "pokemon",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="debilidades",
                        to="pokedex.pokemon",
                    ),
                ),
                (
                    "tipo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="debilidades",
                        to="pokedex.tipo",
                    ),
                ),
            ],
            options={
                "verbose_name": "Debilidad",
                "verbose_name_plural": "Debilidades",
            },
        ),
        migrations.AddField(
            model_name="pokemon",
            name="naturaleza",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="pokemon",
                to="pokedex.naturaleza",
            ),
        ),
        migrations.CreateModel(
            name="Puntos_Base",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("HP", models.IntegerField()),
                ("Ataque", models.IntegerField()),
                ("Defensa", models.IntegerField()),
                ("Ataque_Especial", models.IntegerField()),
                ("Defensa_Especial", models.IntegerField()),
                ("Velocidad", models.IntegerField()),
                (
                    "pokemon",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="puntos_base",
                        to="pokedex.pokemon",
                    ),
                ),
            ],
            options={
                "verbose_name": "Puntos Base",
                "verbose_name_plural": "Puntos Base",
            },
        ),
    ]
