from django.contrib import admin
from .models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "phone_number", "joined_date")
    search_fields = ("first_name", "last_name", "email")
    list_filter = ("joined_date",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "phone_number",
                    "date_of_birth",
                )
            },
        ),
    )
