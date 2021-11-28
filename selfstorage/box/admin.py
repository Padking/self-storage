from django.contrib import admin

from .models import (
    Storage,
    Box,
    BoxOrder,
    Thing,
    SeasonalKeepingOrder
)


@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):
    pass

@admin.register(Box)
class BoxAdmin(admin.ModelAdmin):
    readonly_fields = ['month_rent_price', 'is_rented']

@admin.register(BoxOrder)
class ThingsAdmin(admin.ModelAdmin):
    readonly_fields = ['rent_start', 'rent_end']

@admin.register(Thing)
class ThingsAdmin(admin.ModelAdmin):
    pass

@admin.register(SeasonalKeepingOrder)
class BoxAdmin(admin.ModelAdmin):
    pass
