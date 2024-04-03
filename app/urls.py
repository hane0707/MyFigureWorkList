from django.urls import path
from app.views import SampleAPIView, DateTimeView, FigureListView

urlpatterns = [
    path("sample/", SampleAPIView.as_view(), name="sample"),
    path("datetime/", DateTimeView.as_view(), name="datetime"),
    path("figure/", FigureListView.as_view(), name="figure"),
]