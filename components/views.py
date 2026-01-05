from typing import Type
from django.forms import ModelForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import CPUForm, RAMForm, GPUForm, StorageDriveForm, RemovableStorageDriveForm
from .mixins import ComponentVerboseNameMixin
from .models import Component


FORM_MAP: dict[str, Type[ModelForm]] = {
    'cpu': CPUForm,
    'ram': RAMForm,
    'gpu': GPUForm,
    'storage_drive': StorageDriveForm,
    'removable_storage_drive': RemovableStorageDriveForm,
}

class ComponentListView(ListView):
    model = Component
    template_name = 'components/component_list.html'
    context_object_name = 'component_list'


class ComponentDetailView(ComponentVerboseNameMixin, DetailView):
    model = Component
    template_name = 'components/component_detail.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super(ComponentDetailView, self).get_context_data(**kwargs)

        obj = self.object
        form_class = FORM_MAP[obj._meta.model_name]

        form = form_class(instance=obj)
        for field in form.fields.values():
            field.disabled = True

        context['detail_form'] = form
        return context


class ComponentCreateView(ComponentVerboseNameMixin, CreateView):
    template_name = 'components/component_form.html'

    def get_form_class(self) -> Type[ModelForm]:
        return FORM_MAP[self.kwargs.get('component_type')]

    def get_success_url(self):
        return reverse_lazy('components:component_detail', kwargs={'pk': self.object.pk})


class ComponentUpdateView(ComponentVerboseNameMixin, UpdateView):
    model = Component
    template_name = 'components/component_form.html'

    def get_form_class(self) -> Type[ModelForm]:
        obj = self.get_object()
        return FORM_MAP[obj._meta.model_name]

    def get_success_url(self):
        return reverse_lazy('components:component_detail', kwargs={'pk': self.object.pk})


class ComponentDeleteView(DeleteView):
    model = Component
    template_name = 'components/component_confirm_delete.html'
    success_url = reverse_lazy('components:component_list')
