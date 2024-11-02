# Generated by Django 5.1.2 on 2024-11-02 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("memberships", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="membershipsubscription",
            name="active",
            field=models.BooleanField(
                default=True,
                help_text="Indica si la suscripción está activa",
                verbose_name="Activo",
            ),
        ),
        migrations.AlterField(
            model_name="membership",
            name="duration_days",
            field=models.PositiveIntegerField(
                help_text="Duración de la membresía (solo en membresías personalizadas.)",
                verbose_name="Duración",
            ),
        ),
    ]
