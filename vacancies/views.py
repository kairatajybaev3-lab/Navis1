from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Vacancy
from .serializers import VacancySerializer

class VacancyListView(APIView):
    def get(self, request):
        category = request.GET.get('category')
        level = request.GET.get('level')

        vacancies = Vacancy.objects.all()

        if category:
            vacancies = vacancies.filter(category=category)
        if level:
            vacancies = vacancies.filter(level=level)

        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)