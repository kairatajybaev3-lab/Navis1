from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'email', 'phone', 'created_at']
        phone = PhoneNumberField(region='KG')