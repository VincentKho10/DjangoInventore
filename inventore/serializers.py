import json
from bson import ObjectId
from inventore.services import serviceCreateMetricUnit
from inventore.models import MetricUnit, Unit
from rest_framework import serializers


class MetricUnitSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MetricUnit
        fields = ['id','metric_unit_name']
        read_only_fields = ["id"]

    def create(self, validate_data):
        metric_unit = serviceCreateMetricUnit(validate_data)
        return metric_unit

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ['id','unit_name']