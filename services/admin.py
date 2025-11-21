from django.contrib import admin
from .models import ServicePage, ServiceSection, SidebarItem

class ServiceSectionInline(admin.TabularInline):
    model = ServiceSection
    extra = 0

class SidebarItemInline(admin.TabularInline):
    model = SidebarItem
    extra = 0

@admin.register(ServicePage)
class ServicePageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_published', 'updated')
    prepopulated_fields = {"slug": ("title",)}
    inlines = [ServiceSectionInline, SidebarItemInline]

@admin.register(ServiceSection)
class ServiceSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'page', 'order')

@admin.register(SidebarItem)
class SidebarItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'page', 'order')
