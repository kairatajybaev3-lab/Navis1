from rest_framework import generics
from bid.signals import send_telegram_notification
from blog2.models import Contact
from blog2.serializers import ContactSerializer


class ContactAPIView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        try:
            send_telegram_notification(instance)
        except Exception:
            pass

