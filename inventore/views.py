from django.views import generic
from django.http import HttpResponse
from django.shortcuts import render
from inventore.services import serviceShowAllMetricUnit, serviceShowAllUnit
from inventore.serializers import MetricUnitSerializer, UnitSerializer
from inventore.models import MetricUnit, Unit
from rest_framework import generics

# Create your views here.

class MetricUnitViewApi(generics.ListCreateAPIView):
    queryset = serviceShowAllMetricUnit()
    serializer_class = MetricUnitSerializer

class UnitViewApi(generics.ListCreateAPIView):
    queryset = serviceShowAllUnit()
    serializer_class = UnitSerializer
    
class MetricUnitView(generic.ListView):
    template_name = "inventore/index.html"
    context_object_name = "metric_units"

    def get_queryset(self):
        return [MetricUnitSerializer(mu) for mu in MetricUnit.objects.all()]