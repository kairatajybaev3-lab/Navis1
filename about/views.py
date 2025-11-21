from rest_framework.views import APIView
from rest_framework.response import Response
from yaml import serialize

from .models import AboutInfo, Tool
from .serializers import AboutInfoSerializer, ToolSerializer


class AboutInfoView(APIView):
    def get(self, request):
        about = AboutInfo.objects.first()
        serializer = AboutInfoSerializer(about)
        return Response(serializer.data)


class ToolListView(APIView):
    def get(self, request):
        tools = Tool.objects.all()
        serializer = ToolSerializer(tools, many=True)
        return Response(serializer.data)