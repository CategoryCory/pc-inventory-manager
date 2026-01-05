from django.forms import ModelForm

from .models import CPU, RAM, GPU, StorageDrive, RemovableStorageDrive


class CPUForm(ModelForm):
    class Meta:
        model = CPU
        fields = ('name', 'quantity', 'condition', 'notes', 'cores', 'is_hyperthreaded', 'threads', 'clock_speed_mhz',
                  'integrated_graphics', 'cache_l1_kb', 'cache_l2_kb', 'cache_l3_kb', 'tdp_w', 'socket_type', )


class RAMForm(ModelForm):
    class Meta:
        model = RAM
        fields = ('name', 'quantity', 'condition', 'notes', 'ram_size_mb', 'memory_type', 'speed_mhz', )


class GPUForm(ModelForm):
    class Meta:
        model = GPU
        fields = ('name', 'quantity', 'condition', 'notes', 'vram_mb', 'chipset', 'interface', )


class StorageDriveForm(ModelForm):
    class Meta:
        model = StorageDrive
        fields = ('name', 'quantity', 'condition', 'notes', 'capacity_mb', 'interface', )


class RemovableStorageDriveForm(ModelForm):
    class Meta:
        model = RemovableStorageDrive
        fields = ('name', 'quantity', 'condition', 'notes', 'drive_type', 'interface', )
