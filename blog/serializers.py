from rest_framework import serializers
from blog.models import Service


class ServiceSerializer(serializers.ModelSerializer):
    icon_url = serializers.SerializerMethodField()

    class Meta:
        model = Service
        fields = ['id', 'title', 'description', 'details', 'img', 'icon_url']

    def get_icon_url(self, obj):
        request = self.context.get('request')
        if obj.img:
            return request.build_absolute_uri(obj.img.url)
        return None
