from django.contrib import admin

from .models import (
    Box,
    Storage,
    Thing,
    BoxOrder,
    SeasonalKeepingOrder
)


@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):
    pass

@admin.register(Thing)
class ThingsAdmin(admin.ModelAdmin):
    pass

@admin.register(Box)
class BoxAdmin(admin.ModelAdmin):
    readonly_fields = ['month_rent_price']

@admin.register(BoxOrder)
class ThingsAdmin(admin.ModelAdmin):
    pass

@admin.register(SeasonalKeepingOrder)
class BoxAdmin(admin.ModelAdmin):
    pass
