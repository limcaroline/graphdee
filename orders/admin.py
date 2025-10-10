from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "type",
        "size",
        "price",
        "paid",
        "status",
        "created_at",
    )
    list_filter = (
        "paid",
        "status",
        "type",
        "size",
    )
