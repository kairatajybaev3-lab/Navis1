from django.urls import path
from .views import ContactRequestAPIView

urlpatterns = [
    path('', ContactRequestAPIView.as_view(), name="api-contact"),
]
