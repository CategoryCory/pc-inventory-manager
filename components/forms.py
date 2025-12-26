from django.forms import ModelForm

from .models import CPU


class CPUForm(ModelForm):
    class Meta:
        model = CPU
        fields = ('name', 'quantity', 'cores', 'is_hyperthreaded', 'threads', 'clock_speed_mhz', 'integrated_graphics',
                  'cache_l1_kb', 'cache_l2_kb', 'cache_l3_kb', 'tdp_w', 'socket_type')
