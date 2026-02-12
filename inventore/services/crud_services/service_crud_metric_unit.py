# myapp/services.py
import json
from django.core.exceptions import ValidationError
from django.db import transaction
from inventore.models import MetricUnit, Unit, Tax, Item, ItemEachUnit, ItemMutationHistory

@transaction.atomic
def serviceShowAllMetricUnit():
    metric_unit = MetricUnit.objects.all()
    return metric_unit

@transaction.atomic
def serviceCreateMetricUnit(data):
    """
    Creates a user and associated profile in a single transaction.
    Raises ValidationError if inputs are invalid.
    """
    metric_unit_name = data['metric_unit_name']

    if not metric_unit_name:
        raise ValidationError("metric unit name are required.")

    metric_unit = MetricUnit.objects.create(metric_unit_name)

    metric_unit.save()

    return metric_unit

@transaction.atomic
def serviceUpdateMetricUnit(data):
    id = data['id']
    metric_unit_name = data['metric_unit_name']

    if not metric_unit_name:
        raise ValidationError("metric unit name are required")

    metric_unit = MetricUnit.objects.get(id=id)

    if not metric_unit:
        raise ValidationError("no selected update")

    metric_unit.metric_unit_name = metric_unit_name
    metric_unit.save()
    return metric_unit

    