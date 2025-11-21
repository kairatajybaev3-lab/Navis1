from django.urls import path
from blog.views import ServiceListView, ServiceDetailView


urlpatterns = [
    path('', ServiceListView.as_view(), name='service-list'),
    path('<int:pk>/', ServiceDetailView.as_view(), name="service-detail"),
]
