from rest_framework import serializers
from .models import ServicePage, ServiceSection, SidebarItem


class ServiceSectionSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = ServiceSection
        fields = ('id', 'title', 'content', 'image_url', 'order')

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        if obj.image:
            return obj.image.url
        return None


class SidebarItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SidebarItem
        fields = ('id', 'title', 'link', 'order')


class ServicePageSerializer(serializers.ModelSerializer):
    sections = ServiceSectionSerializer(many=True, read_only=True)
    sidebar_items = SidebarItemSerializer(many=True, read_only=True)
    hero_image_url = serializers.SerializerMethodField()

    class Meta:
        model = ServicePage
        fields = ('id', 'title', 'slug', 'subtitle', 'hero_text', 'hero_image_url', 'sections', 'sidebar_items', 'is_published', 'updated')

    def get_hero_image_url(self, obj):
        request = self.context.get('request')
        if obj.hero_image and request:
            return request.build_absolute_uri(obj.hero_image.url)
        if obj.hero_image:
            return obj.hero_image.url
        return None