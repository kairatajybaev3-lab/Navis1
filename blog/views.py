from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView


from blog.models import Service
from blog.serializers import ServiceSerializer


class ServiceListView(APIView):
    def get(self, request):
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True, context={'request': request})
        return Response(serializer.data)


class ServiceDetailView(APIView):
    def get(self, request, pk):
        service = get_object_or_404(Service, pk=pk)
        serializer = ServiceSerializer(service, context={'request': request})
        return Response(serializer.data)
