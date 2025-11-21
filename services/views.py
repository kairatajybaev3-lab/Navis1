from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import ServicePage
from .serializers import ServicePageSerializer

class ServicePageListView(generics.ListAPIView):

    queryset = ServicePage.objects.filter(is_published=True)
    serializer_class = ServicePageSerializer
    permission_classes = [AllowAny]


class ServicePageDetailView(generics.RetrieveAPIView):

    queryset = ServicePage.objects.all()
    serializer_class = ServicePageSerializer
    lookup_field = 'slug'
    permission_classes = [AllowAny]


