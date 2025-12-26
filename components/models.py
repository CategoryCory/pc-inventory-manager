from django.db import models
from polymorphic.models import PolymorphicModel

from .enums import CPUSocket, RAMType, ExpansionBus, StorageInterface, RemovableMedia


class Component(PolymorphicModel):
    name = models.CharField(max_length=100, verbose_name='Component Name')
    quantity = models.IntegerField(default=1, verbose_name='Quantity')

    def __str__(self) -> str:
        return self.name


class CPU(Component):
    cores = models.IntegerField(default=1, verbose_name='CPU Cores')
    is_hyperthreaded = models.BooleanField(default=False, verbose_name='Hyper-Threaded')
    threads = models.IntegerField(null=True, blank=True, verbose_name='CPU Threads')
    clock_speed_mhz = models.IntegerField(verbose_name='Clock Speed (MHz)')
    integrated_graphics = models.BooleanField(default=False, verbose_name='Integrated Graphics')
    cache_l1_kb = models.IntegerField(null=True, blank=True, verbose_name='L1 Cache (KB)')
    cache_l2_kb = models.IntegerField(null=True, blank=True, verbose_name='L2 Cache (KB)')
    cache_l3_kb = models.IntegerField(null=True, blank=True, verbose_name='L3 Cache (KB)')
    tdp_w = models.IntegerField(null=True, blank=True, verbose_name='Thermal Design Power (W)')
    socket_type = models.CharField(max_length=50,
                                   blank=True,
                                   choices=CPUSocket,
                                   default=CPUSocket.SOCKET_1,
                                   verbose_name='Socket Type')

    @property
    def clock_speed_ghz(self) -> float:
        return round(self.clock_speed_mhz / 1000, 2)

    class Meta:
        verbose_name = 'CPU'
        verbose_name_plural = 'CPUs'


class RAM(Component):
    ram_size_mb = models.IntegerField(verbose_name='RAM Size (MB)')
    memory_type = models.CharField(max_length=50, choices=RAMType, default=RAMType.FPM, verbose_name='Memory Type')
    speed_mhz = models.IntegerField(null=True, blank=True, verbose_name='RAM Speed (MHz)')

    @property
    def ram_size_gb(self) -> float:
        return round(self.ram_size_mb / 1000, 2)

    @property
    def speed_ghz(self) -> float:
        return round(self.speed_mhz / 1000, 2)

    class Meta:
        verbose_name = 'RAM Module'
        verbose_name_plural = 'RAM Modules'


class GPU(Component):
    vram_mb = models.IntegerField(verbose_name='VRAM Size (MB)')
    chipset = models.CharField(max_length=100, blank=True, null=True, verbose_name='Chipset Name')
    interface = models.CharField(max_length=50, choices=ExpansionBus, verbose_name='Interface Name')

    @property
    def vram_gb(self) -> float:
        return round(self.vram_mb / 1000, 2)

    class Meta:
        verbose_name = 'GPU'
        verbose_name_plural = 'GPUs'


class StorageDrive(Component):
    capacity_mb = models.IntegerField(verbose_name='Storage Drive Capacity (MB)')
    interface = models.CharField(max_length=50, choices=StorageInterface, verbose_name='Interface Name')

    @property
    def capacity_gb(self) -> float:
        return round(self.capacity_mb / 1000, 2)

    class Meta:
        verbose_name = 'Storage Drive'
        verbose_name_plural = 'Storage Drives'


class RemovableStorageDrive(Component):
    drive_type = models.CharField(max_length=50, choices=RemovableMedia, verbose_name='Drive Type')
    interface = models.CharField(max_length=50, choices=StorageInterface, verbose_name='Interface Name')

    class Meta:
        verbose_name = 'Removable Storage Drive'
        verbose_name_plural = 'Removable Storage Drives'
