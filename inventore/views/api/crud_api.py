from inventore.services import serviceShowAllMetricUnit, serviceShowAllUnit
from inventore.serializers import MetricUnitSerializer, UnitSerializer
from rest_framework import generics

# Create your views here.
class UnitViewApi(generics.ListCreateAPIView):
    queryset = serviceShowAllUnit()
    serializer_class = UnitSerializer

class MetricUnitViewApi(generics.ListCreateAPIView):
    queryset = serviceShowAllMetricUnit()
    serializer_class = MetricUnitSerializer