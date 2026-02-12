from django.utils import timezone
from decimal import Decimal
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from django_mongodb_backend.models import EmbeddedModel
from django_mongodb_backend.fields import EmbeddedModelField

# Create your models here.

# MetricUnit, Unit, Tax, Item, ItemEachUnit, ItemMutationHistory

class MetricUnit(models.Model):
    metric_unit_name = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.metric_unit_name
    
class Unit(models.Model):
    unit_name = models.CharField(max_length=100)
    metric_unit = models.ForeignKey(MetricUnit, on_delete=models.CASCADE, default=1)
    ratio = models.IntegerField(default=1)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.unit_name
    
class Tax(models.Model):
    tax_value = models.DecimalField(decimal_places=2, max_digits=5, unique=True, validators=[
        MinValueValidator(1),
        MaxValueValidator(100)
    ])
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.tax_value)

class Item(models.Model):
    item_name = models.CharField(max_length=200)
    item_code = models.CharField(max_length=200)
    quantity = models.IntegerField()
    grand_total = models.DecimalField(default=0, editable=False, decimal_places=2, max_digits=20)
    metric_unit = models.ForeignKey(MetricUnit,on_delete=models.DO_NOTHING)
    
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.item_name
    
class ItemEachUnit(models.Model):
    quantity = models.IntegerField()
    unit = models.ForeignKey(Unit, on_delete=models.DO_NOTHING, null=True, blank=True)
    metric_unit = models.ForeignKey(MetricUnit, on_delete=models.DO_NOTHING, null=False, blank=False)
    unit_price = models.DecimalField(default=1, decimal_places=2, max_digits=20) 
    base_total = models.DecimalField(default=0, editable=False, decimal_places=2, max_digits=20)
    tax = models.ForeignKey(Tax, on_delete=models.DO_NOTHING, default=1)
    total = models.DecimalField(default=0, editable=False, decimal_places=2, max_digits=20)
    
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    id_code = models.CharField(editable=False)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)
    
class ItemMutationHistory(models.Model):
    title = models.CharField(max_length=50, editable=False)
    description = models.TextField(max_length=200, editable=False)
    item_e_unit = models.ForeignKey(ItemEachUnit, default=1, on_delete=models.DO_NOTHING, null=False, blank=False)
    mutation_quantity = models.DecimalField(default=0, decimal_places=2, max_digits=20)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title