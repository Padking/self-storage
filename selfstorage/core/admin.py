from django.contrib import admin

from .models import (
    Box,
    Place,
    Storage,
)


@admin.register(Place, Storage, Box)
class PlaceAdmin(admin.ModelAdmin):
    pass
