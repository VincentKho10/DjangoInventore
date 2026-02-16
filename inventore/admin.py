from django.contrib import admin

from .models import ItemEachUnit, MetricUnit, Item, Tax, ItemMutationHistory, Unit
# Register your models here.


@admin.register(MetricUnit)
class MetricUnitAdmin(admin.ModelAdmin):
    list_display = ('metric_unit_name',)
    search_fields = ('metric_unit_name',)

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ('unit_name',)
    search_fields = ('unit_name',)

@admin.register(Tax)
class TaxAdmin(admin.ModelAdmin):
    list_display = ('tax_value',)
    search_fields = ('tax_value',)

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('item_code', 'item_name', 'metric_unit', 'quantity', 'grand_total')
    search_fields = ('item_name',)
    
@admin.register(ItemEachUnit)
class ItemEachUnitAdmin(admin.ModelAdmin):
    list_display = ('quantity', 'unit', 'metric_unit', 'unit_price', 'base_total', 'tax', 'item', 'id_code')
    search_fields = ('item_name',)
    

@admin.register(ItemMutationHistory)
class ItemMutationHistoryAdmin(admin.ModelAdmin):
    list_display = ('title','description', 'item_e_unit', 'mutation_quantity')
    search_fields = ('title',)