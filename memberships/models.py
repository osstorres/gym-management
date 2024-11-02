from django.db import models
from django.utils.translation import gettext_lazy as _
from customers.models import Client


class MembershipType(models.TextChoices):
    WEEKLY = "weekly", _("Semanal")
    BIWEEKLY = "biweekly", _("Quincenal")
    MONTHLY = "monthly", _("Mensual")
    SEMIANNUAL = "semiannual", _("Semestral")
    ANNUAL = "annual", _("Anual")
    CUSTOM = "custom", _("Custom")
    SINGLE_VISIT = "single_visit", _("Visita única")


class Membership(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        help_text=_("Nombre de la membresía"),
        verbose_name=_("Nombre"),
    )
    membership_type = models.CharField(
        max_length=20,
        choices=MembershipType.choices,
        default=MembershipType.CUSTOM,
        help_text=_("Tipo de membresía"),
        verbose_name="Tipo",
    )
    duration_days = models.PositiveIntegerField(
        help_text=_("Duración de la membresía (solo en membresías personalizadas.)"),
        verbose_name="Duración",
    )
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        help_text=_("Precio de la membresía"),
        verbose_name="Precio",
    )

    def __str__(self):
        return f"{self.name} :: ({self.get_membership_type_display()})"

    class Meta:
        verbose_name = "Membresía"
        verbose_name_plural = "Membresías"


class MembershipSubscription(models.Model):
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name="subscriptions",
        verbose_name="Cliente",
    )
    membership = models.ForeignKey(
        Membership,
        on_delete=models.PROTECT,
        related_name="subscriptions",
        verbose_name="Membresía",
    )
    active = models.BooleanField(
        default=True,
        verbose_name="Activo",
        help_text="Indica si la suscripción está activa",
    )
    start_date = models.DateField(
        help_text=_("Start date of the subscription"),
        verbose_name="Fecha de inicio de la suscripción",
    )
    end_date = models.DateField(
        help_text=_("End date of the subscription"),
        verbose_name="Fecha de finalización de " "la suscripción",
    )

    def __str__(self):
        return f"{self.client} - {self.membership} desde {self.start_date} a {self.end_date}"

    class Meta:
        verbose_name = "Suscripción"
        verbose_name_plural = "Suscripciones"
