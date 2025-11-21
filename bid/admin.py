from django.contrib import admin
from .models import ContactRequest

@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "phone", "created_at", "processed")
    list_filter = ("processed",)
    search_fields = ("name", "phone", "message")
    readonly_fields =  ("created_at",)