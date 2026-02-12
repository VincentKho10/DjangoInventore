from django.forms import ValidationError
from inventore.models import Tax
from django.db import transaction

@transaction.atomic
def serviceShowAllTax():
    tax_value = Tax.objects.all()
    return tax_value

@transaction.atomic
def serviceGetOneTax(tax_tofind):
    tax = Tax.objects.get(tax_tofind.id)
    return tax

@transaction.atomic
def serviceCreateTax(data):
    print(data)
    tax_value = data['tax_value']/100
    
    if not tax_value:
        raise ValidationError('tax value are required')
    
    tax = Tax.objects.create(tax_value)
    print(tax)
    return tax

@transaction.atomic
def serviceUpdateTax(data):
    print(data['tax_value'])
    tax_value = data['tax_value']*100
    
    if not tax_value:
        raise ValidationError('tax value are required')
    
    tax = Tax.objects.update(tax_value/100)
    print(tax)
    return tax