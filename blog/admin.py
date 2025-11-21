from django.contrib import admin
from django.utils.html import format_html
from  .models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description")
    search_fields = ("title",)

    def preview(self, obj):
        if obj.icon:
            return format_html('<img src="{}" width="50" height="50" style="object-fit:cover; border-radius:5px;"/>',
                                obj.icon.url)
        return "—"

    preview.short_description = "Иконка"
