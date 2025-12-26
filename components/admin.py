from django.contrib import admin
from polymorphic.admin import (
    PolymorphicParentModelAdmin,
    PolymorphicChildModelAdmin,
)

from .models import (
    Component,
    CPU,
    RAM,
    GPU,
    StorageDrive,
    RemovableStorageDrive,
)


@admin.register(Component)
class ComponentParentAdmin(PolymorphicParentModelAdmin):
    base_model = Component
    child_models = (
        CPU,
        RAM,
        GPU,
        StorageDrive,
        RemovableStorageDrive,
    )

    list_display = ("name", "polymorphic_ctype", )
    list_filter = ("polymorphic_ctype", )
    search_fields = ("name", )


class ComponentChildAdmin(PolymorphicChildModelAdmin):
    base_model = Component
    show_in_index = True

    list_display = ("name", )
    list_filter = ()
    search_fields = ("name", )


@admin.register(CPU)
class CPUAdmin(ComponentChildAdmin):
    base_model = CPU


@admin.register(RAM)
class RAMAdmin(ComponentChildAdmin):
    base_model = RAM


@admin.register(GPU)
class GPUAdmin(ComponentChildAdmin):
    base_model = GPU


@admin.register(StorageDrive)
class StorageDriveAdmin(ComponentChildAdmin):
    base_model = StorageDrive


@admin.register(RemovableStorageDrive)
class RemovableStorageDriveAdmin(ComponentChildAdmin):
    base_model = RemovableStorageDrive
