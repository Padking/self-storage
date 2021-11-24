from django.contrib import admin

from .models import (
    Thing,
    Photo,
)


@admin.register(Thing, Photo)
class ThingsAdmin(admin.ModelAdmin):
    pass
