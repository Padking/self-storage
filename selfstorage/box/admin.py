from django.contrib import admin

from .models import (
    Box,
    Photo,
    Place,
    Storage,
    Thing,
)


@admin.register(Place, Storage)
class PlaceAdmin(admin.ModelAdmin):
    pass


@admin.register(Thing, Photo)
class ThingsAdmin(admin.ModelAdmin):
    pass

@admin.register(Box)
class BoxAdmin(admin.ModelAdmin):
    readonly_fields = ['month_rent_price']
