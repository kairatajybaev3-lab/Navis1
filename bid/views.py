from rest_framework import generics
from .models import ContactRequest
from .serializers import ContactRequestSerializer
from .signals import send_telegram_notification

class ContactRequestAPIView(generics.CreateAPIView):
    queryset = ContactRequest.objects.all()
    serializer_class = ContactRequestSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        try:
            send_telegram_notification(instance)
        except Exception:
            pass