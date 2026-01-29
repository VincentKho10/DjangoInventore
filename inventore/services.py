# myapp/services.py
import json
from django.core.exceptions import ValidationError
from django.db import transaction
from .models import MetricUnit, Unit, Tax, Item, ItemEachUnit, ItemMutationHistory

@transaction.atomic
def serviceShowAllMetricUnit():
    metric_unit = MetricUnit.objects.all()
    return metric_unit

@transaction.atomic
def serviceCreateMetricUnit(validate_data):
    """
    Creates a user and associated profile in a single transaction.
    Raises ValidationError if inputs are invalid.
    """
    metric_unit_name = validate_data['metric_unit_name']

    if not metric_unit_name:
        raise ValidationError("metric unit name are required.")

    metric_unit = MetricUnit.objects.create(metric_unit_name)

    return metric_unit