# myapp/services.py
import json
from django.core.exceptions import ValidationError
from django.db import transaction
from inventore.serializers import UnitSerializer
from inventore.models import Unit, Unit, Tax, Item, ItemEachUnit, ItemMutationHistory

@transaction.atomic
def serviceShowAllUnit():
    unit = Unit.objects.all()
    return unit

@transaction.atomic
def serviceCreateUnit(data):
    """
    Creates a user and associated profile in a single transaction.
    Raises ValidationError if inputs are invalid.
    """
    unit = UnitSerializer(data)
    unit.is_valid()
    
    print(unit.data)
    unit = Unit.objects.create(unit.data)

    # unit.save()
    return unit

@transaction.atomic
def serviceUpdateUnit(data):
    unit: Unit = UnitSerializer(data)

    unit.is_valid()
    
    uunit = Unit.objects.get(id=unit.id)

    if not unit:
        raise ValidationError("no selected update")

    uunit.unit_name = unit.unit_name
    # uunit.save()
    return uunit

    