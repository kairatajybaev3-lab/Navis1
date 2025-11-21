from rest_framework import serializers
from .models import ContactRequest
from .utils import normalize_and_validate_phone


def validate_phone(value):
    try:
        normalized = normalize_and_validate_phone(value)
    except ValueError as e:
        raise serializers.ValidationError(str(e))
    return normalized


class ContactRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactRequest
        fields = ("id", "name", "phone", "message", "created_at")
        read_only_fields = ('id', 'created_at')

        def create(self, validated_data):
            return super().create(validated_data)