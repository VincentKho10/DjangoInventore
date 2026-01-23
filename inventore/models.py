from django.utils import timezone
from decimal import Decimal
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from django_mongodb_backend.models import EmbeddedModel
from django_mongodb_backend.fields import EmbeddedModelField

# Create your models here.

class MetricUnit(models.Model):
    metric_unit_name = models.CharField(max_length=5)
    
    def __str__(self):
        return self.metric_unit_name
    
class Unit(models.Model):
    unit_name = models.CharField(max_length=5)

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
    metric_unit = models.ForeignKey(MetricUnit,on_delete=models.DO_NOTHING)
    unit = models.ForeignKey(Unit, on_delete=models.DO_NOTHING, null=True, blank=True)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(decimal_places=2, max_digits=20) 
    base_total = models.DecimalField(editable=False, decimal_places=2, max_digits=20)
    tax = models.ForeignKey(Tax, on_delete=models.DO_NOTHING)
    grand_total = models.DecimalField(editable=False, decimal_places=2, max_digits=20)
    package_ratio = models.DecimalField(default=1, decimal_places=2, max_digits=20, validators=[MinValueValidator(int(1))])
    package_quantity = models.IntegerField(editable=False)
    
    def save(self, *args, **kwargs):
        if self.unit == None:
            self.package_quantity = self.quantity
        else:
            self.package_quantity = self.quantity / self.package_ratio
        self.base_total = (self.unit_price * self.quantity)
        self.grand_total = self.base_total * ((self.tax.tax_value + 1) / 1)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.item_name
    
class ItemEachUnit(models.Model):
    item_name = models.CharField(max_length=200)
    item_code = models.CharField(max_length=200)
    metric_unit = models.ForeignKey(MetricUnit,on_delete=models.DO_NOTHING)
    unit = models.ForeignKey(Unit, on_delete=models.DO_NOTHING, null=True, blank=True)
    quantity = models.IntegerField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    id_code = models.URLField(editable=False)

    def save(self, *args, **kwargs):
        self.item_name = self.item.item_name
        self.item_code = self.item.item_code
        self.metric_unit = self.item.metric_unit
        self.unit = self.item.unit
        self.quantity = self.item.package_quantity
        super().save(*args,**kwargs)
    
class ItemMutationHistory(models.Model):
    title = models.CharField(max_length=50, editable=False)
    description = models.TextField(max_length=200, editable=False)
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    quantity = models.DecimalField(decimal_places=2, max_digits=20)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        quantityresult = self.item.quantity + self.quantity
        self.title = ("Increase " if self.quantity >= 0 else "Decrease ") + "{} on {}_{} by root ".format(self.quantity, self.item.item_code, self.item.item_name)
        self.description = self.title + " from {} to {}".format(self.item.quantity, quantityresult) 
        self.item.quantity = quantityresult
        self.item.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
