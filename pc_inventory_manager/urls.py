from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pages.urls')),
    path('components/', include('components.urls')),
    path('admin/', admin.site.urls),
]
