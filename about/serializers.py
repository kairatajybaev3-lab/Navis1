from rest_framework import serializers
from .models import AboutInfo, Tool

class AboutInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutInfo
        fields = '__all__'

    def get_icon_url(self, obj):
        request = self.context.get('request')
        if obj.founder_image:
            return request.build_absolute_uri(obj.founder_image.url)
        return None

class ToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tool
        fields = '__all__'

    def get_icon_url(self, obj):
        request = self.context.get('request')
        if obj.icon_img:
            return request.build_absolute_uri(obj.icon_img.url)
        return None
