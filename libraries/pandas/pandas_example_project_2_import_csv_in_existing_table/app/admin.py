from django.contrib import admin
from .models import *


class MedicineAdmin(admin.ModelAdmin):
    list_display = (
    'name', 'strength', 'generic_name', 'manufacturer', 'supplier', 'pack_size', 'doses_form',
    'department', 'image')
    list_filter = ('manufacturer', 'supplier', 'pack_size', 'doses_form', 'department', 'medicine_type')
    search_fields = ('name', 'generic_name__name', 'manufacturer__name', 'supplier__name')
    fieldsets = (
        ('General Information', {
            'fields': (
            'name', 'strength', 'generic_name', 'manufacturer', 'supplier', 'doses_form', 'department',
            'medicine_type')
        }),
        ('Packaging Information', {
            'fields': ('pack_size',)
        }),
        ('Image Information', {
            'fields': ('image',)
        }),
    )
    list_per_page = 20
    list_select_related = ('manufacturer', 'supplier')


class GenericAdmin(admin.ModelAdmin):
    list_display = ('generic_id', 'generic_name',)
    search_fields = ('generic_name',)