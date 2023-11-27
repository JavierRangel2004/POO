# urls.py del proyecto Final_PDI

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from procesamiento_imagenes import views as image_views  # Asegúrate de importar tu vista

urlpatterns = [
    path('admin/', admin.site.urls),
    path('procesamiento_imagenes/', include('procesamiento_imagenes.urls')),
    path('', image_views.image_upload_view, name='home'),  # Ruta para la vista de carga de imágenes
    # ... otras rutas
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
