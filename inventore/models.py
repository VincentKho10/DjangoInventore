from decimal import Decimal
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from django_mongodb_backend.models import EmbeddedModel
from django_mongodb_backend.fields import EmbeddedModelField

# Create your models here.

class UnitMetric(models.Model):
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
    item_code = models.CharField(max_length=200)
    unit_metric = models.ForeignKey(UnitMetric,on_delete=models.DO_NOTHING)
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
    
class ItemMutationHistory(models.Model):
    title = models.CharField(max_length=50, editable=False)
    description = models.TextField(max_length=200, editable=False)
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    quantity = models.DecimalField(decimal_places=2)

    def save(self, *args, **kwargs):
        quantityresult = self.item.quantity + self.quantity
        self.title = ("Increase " if self.quantity >= 0 else "Decrease ") + "%d at %s_%s by root ".format(self.quantity, self.item.item_code, self.item.item_name)
        self.description = self.title + " from %d to %d".format(self.item.quantity, quantityresult) 
        self.item.quantity = quantityresult
        self.item.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
