from django.contrib import admin

from .models import (
    Box,
    Photo,
    Place,
    Storage,
    Thing,
)


@admin.register(Place, Storage, Box)
class PlaceAdmin(admin.ModelAdmin):
    pass


@admin.register(Thing, Photo)
class ThingsAdmin(admin.ModelAdmin):
    pass
