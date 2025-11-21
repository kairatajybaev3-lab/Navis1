from django.urls import path
from about.views import AboutInfoView, ToolListView


urlpatterns = [
    path('', AboutInfoView.as_view(), name='about_info'),
    path('tools/', ToolListView.as_view(), name='tools'),
]