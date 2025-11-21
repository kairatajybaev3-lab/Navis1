from django.db import models
from django.utils.text import slugify


class ServicePage(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    subtitle = models.CharField(max_length=255, blank=True)
    hero_image = models.ImageField(upload_to='services/hero/', blank=True, null=True)
    hero_text = models.CharField(max_length=255, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created',)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ServiceSection(models.Model):
    page = models.ForeignKey(ServicePage, related_name='sections', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to='services/sections', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('order',)
    def __str__(self):
        return f"{self.page.title} - {self.title}"


class SidebarItem(models.Model):
    page = models.ForeignKey(ServicePage, related_name='sidebar_items', on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    link = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('order',)

    def __str__(self):
        return self.title

