from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .api import vehicle_models_view, vehicle_images_view
from .views import home

urlpatterns = [
    path('', home),
    path('vehicle_models_view/', vehicle_models_view, name="vehicle_models_view"),
    path('vehicle_images_view/', vehicle_images_view, name="vehicle_images_view"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
