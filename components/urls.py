from django.urls import path

from .views import ComponentListView, ComponentDetailView, ComponentCreateView, ComponentUpdateView, ComponentDeleteView

app_name = 'components'
urlpatterns = [
    path('', ComponentListView.as_view(), name='component_list'),
    path('<int:pk>/', ComponentDetailView.as_view(), name='component_detail'),
    path('add/<str:component_type>/', ComponentCreateView.as_view(), name='component_create'),
    path('<int:pk>/edit/', ComponentUpdateView.as_view(), name='component_update'),
    path('<int:pk>/delete/', ComponentDeleteView.as_view(), name='component_delete'),
]
