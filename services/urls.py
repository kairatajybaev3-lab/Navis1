from django.urls import path
from . import views

urlpatterns = [
    path('', views.ServicePageListView.as_view(), name='serviceable-list'),
    path('<slug:slug>/', views.ServicePageDetailView.as_view(), name='serviceable-detail'),
]