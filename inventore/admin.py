from django.contrib import admin

from .models import MetricUnit, Item, Tax, ItemMutationHistory, Unit
# Register your models here.


@admin.register(MetricUnit)
class MetricUnitAdmin(admin.ModelAdmin):
    list_display = ('metric_unit_name',)
    search_fields = ('metric_unit_name',)

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ('unit_name',)
    search_fields = ('unit_name',)

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('item_code', 'item_name', 'metric_unit', 'quantity', 'unit_price', 'tax', 'grand_total', 'package_desc')
    search_fields = ('item_name',)

    @admin.display(description="Packaging Description")
    def package_desc(self, obj):
        if(obj.unit):
            return "{} {} @{} {}".format(obj.package_quantity, obj.unit, obj.package_ratio, obj.metric_unit)
        return "{} {}".format(obj.package_quantity, obj.metric_unit)

@admin.register(Tax)
class TaxAdmin(admin.ModelAdmin):
    list_display = ('tax_name',)
    search_fields = ('tax_name',)

@admin.register(ItemMutationHistory)
class ItemMutationHistoryAdmin(admin.ModelAdmin):
    list_display = ('title','description')
    search_fields = ('title',)