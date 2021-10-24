from django.contrib import admin
from django.db import models
from .models import VehicleManufacturer, VehicleModel, VehicleModelImage
from import_export.admin import ImportExportModelAdmin


class VehicleModelTabularinline(admin.TabularInline):
    model = VehicleModel


@admin.register(VehicleManufacturer)
class VehicleManufacturerAdmin(ImportExportModelAdmin):
    inlines = [VehicleModelTabularinline]

# -----------------------------------------------------


class VehicleModelImageTabularinline(admin.TabularInline):
    model = VehicleModelImage


@admin.register(VehicleModel)
class VehicleModelAdmin(ImportExportModelAdmin):
    inlines = [VehicleModelImageTabularinline]

# -----------------------------------------------------


admin.site.register(VehicleModelImage)
