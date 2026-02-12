import json
from bson import ObjectId
from inventore.services.crud_services.service_crud_tax import serviceCreateTax
from inventore.services import serviceCreateMetricUnit
from inventore.models import Item, MetricUnit, Tax, Unit
from rest_framework import serializers


class MetricUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetricUnit
        fields = ['id','metric_unit_name']
        read_only_fields = ["id"]

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ['id','unit_name']

class TaxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tax
        fields = ['id', 'tax_value']

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'item_code', 'item_name', 'metric_unit', 'quantity', 'grand_total']