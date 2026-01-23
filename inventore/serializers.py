from bson import ObjectId
from inventore.models import MetricUnit, Unit
from rest_framework import serializers

class ObjectIdField(serializers.Field):
    def to_representation(self, value):
        return str(value)
    
    def to_internal_value(self, value):
        return ObjectId(value)

class MetricUnitSerializer(serializers.ModelSerializer):
    id = ObjectIdField()

    class Meta:
        model = MetricUnit
        fields = ['id', 'metric_unit_name']

class UnitSerializer(serializers.ModelSerializer):
    id = ObjectIdField()

    class Meta:
        model = Unit
        fields = ['id','unit_name']