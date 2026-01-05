from typing import Any


class ComponentVerboseNameMixin:
    def get_component_verbose_name(self) -> str:
        if getattr(self, 'object', None) is not None:
            return self.object._meta.verbose_name

        form_class = self.get_form_class()
        return form_class._meta.model._meta.verbose_name

    def get_context_data(self, **kwargs: dict[str, Any]) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['component_name'] = self.get_component_verbose_name()
        return context
