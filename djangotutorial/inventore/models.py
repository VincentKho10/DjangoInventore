from decimal import Decimal
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from django_mongodb_backend.models import EmbeddedModel
from django_mongodb_backend.fields import EmbeddedModelField

# Create your models here.

class Unit(models.Model):
    unit_name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.unit_name
    
class Tax(models.Model):
    tax_name = models.CharField(editable=False, max_length=4)
    tax_value = models.DecimalField(default=0.11, decimal_places=2, max_digits=3, unique=True, validators=[
        MinValueValidator(Decimal('0.01')),
        MaxValueValidator(Decimal('1'))
    ])

    def save(self, *args, **kwargs):
        self.tax_name = str(self.tax_value).split(".")[1] + " %"
        super().save(*args,**kwargs)

    def __str__(self):
        return self.tax_name

class Item(models.Model):
    item_name = models.CharField(max_length=200)
    unit = models.ForeignKey(Unit,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    unit_price = models.DecimalField(default=0, decimal_places=2, max_digits=20) 
    base_total = models.DecimalField(editable=False, decimal_places=2, max_digits=20)
    tax = models.ForeignKey(Tax, on_delete=models.CASCADE)
    grand_total = models.DecimalField(editable=False, decimal_places=2, max_digits=20)
    
    def save(self, *args, **kwargs):
        self.base_total = (self.unit_price * self.quantity)
        self.grand_total = self.base_total * ((self.tax.tax_value + 1) / 1)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.item_name