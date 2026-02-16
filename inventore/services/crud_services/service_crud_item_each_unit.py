# myapp/services.py
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.db import transaction
from inventore.serializers import UnitSerializer
from inventore.models import MetricUnit, Unit, Unit, Tax, Item, ItemEachUnit, ItemMutationHistory
from django.core.management import call_command

@transaction.atomic
def serviceShowAllItemEachUnit():
    unit = Unit.objects.all()
    return unit

@transaction.atomic
def serviceCreateItemEachUnit(data):
    """
    Creates a user and associated profile in a single transaction.
    Raises ValidationError if inputs are invalid.
    """
    n = data.quantity / data.unit.ratio

    tobe_created = []

    for i in range(1,int(n),1):
        nieu = ItemEachUnit()
        nieu.item = data.item
        nieu.item.grand_total = data.item.grand_total + data.base_total
        nieu.quantity = data.quantity
        nieu.base_total = float(data.unit_price) * (data.quantity/n)
        nieu.unit_price = data.unit_price
        nieu.id_code = "test"
        nieu.unit = data.unit
        nieu.metric_unit = data.unit.metric_unit
        nieu.updated_at = timezone.now()
        nieu.created_at = timezone.now()
        tobe_created.append(nieu)
    print(nieu)

    # created_bulk = ItemEachUnit.objects.bulk_create(tobe_created)

    return None

@transaction.atomic
def serviceUpdateItemEachUnit(data):
    unit: Unit = UnitSerializer(data)

    unit.is_valid()
    
    uunit = Unit.objects.get(id=unit.id)

    if not unit:
        raise ValidationError("no selected update")

    uunit.unit_name = unit.unit_name
    # uunit.save()
    return uunit

    