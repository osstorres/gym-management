from django.db import models


class Client(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Nombre")
    last_name = models.CharField(
        max_length=50, verbose_name="Apellidos", null=True, blank=True
    )
    email = models.EmailField(unique=True, verbose_name="Email", null=True, blank=True)
    phone_number = models.CharField(
        max_length=15, blank=True, null=True, verbose_name="Telefono"
    )
    date_of_birth = models.DateField(
        blank=True, null=True, verbose_name="Fecha de nacimiento"
    )
    joined_date = models.DateField(auto_now_add=True, verbose_name="Fecha de registro")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
