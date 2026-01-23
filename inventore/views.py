from django.shortcuts import render
from inventore.serializers import MetricUnitSerializer, UnitSerializer
from inventore.models import MetricUnit, Unit
from rest_framework import generics

# Create your views here.

class MetricUnitView(generics.ListCreateAPIView):
    queryset = MetricUnit.objects.all()
    serializer_class = MetricUnitSerializer

class UnitView(generics.ListCreateAPIView):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer