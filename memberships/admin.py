from django.contrib import admin
from .models import Membership, MembershipSubscription


@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ("name", "membership_type", "duration_days", "price")
    list_filter = ("membership_type",)
    search_fields = ("name",)
    fieldsets = (
        (None, {"fields": ("name", "membership_type", "duration_days", "price")}),
    )


@admin.register(MembershipSubscription)
class MembershipSubscriptionAdmin(admin.ModelAdmin):
    list_display = ("client", "membership", "start_date", "end_date")
    list_filter = ("membership", "start_date")
    search_fields = ("client__first_name", "client__last_name", "membership__name")
    fieldsets = (
        (None, {"fields": ("client", "membership", "start_date", "end_date")}),
    )
