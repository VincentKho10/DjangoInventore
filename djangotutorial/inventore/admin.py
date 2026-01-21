from django.contrib import admin

from .models import Unit, Item, Tax
# Register your models here.


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ('unit_name',)
    search_fields = ('unit_name',)

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('item_name',)
    search_fields = ('item_name',)

@admin.register(Tax)
class TaxAdmin(admin.ModelAdmin):
    list_display = ('tax_name',)
    search_fields = ('tax_name',)