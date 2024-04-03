from django.views.generic.base import TemplateView
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

import datetime


class SampleAPIView(APIView):
    def get(self, request):
        return Response("OK", status=status.HTTP_200_OK)


class DateTimeView(APIView):
    def get(self, request):
        datetime_str = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        return Response(datetime_str, status=status.HTTP_200_OK)
    
class FigureListView(APIView):
    def get(self, request):
        return Response("figure list OK", status=status.HTTP_200_OK)


class IndexView(TemplateView):
    template_name = "index.html"