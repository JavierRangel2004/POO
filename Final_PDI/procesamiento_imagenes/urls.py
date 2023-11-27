# urls.py dentro de la aplicación procesamiento_imagenes

from django.urls import path
from . import views  # Importa las vistas de la aplicación

urlpatterns = [
    path('upload/', views.image_upload_view, name='image_upload'),  # Ruta para cargar imágenes
    # ... aquí puedes añadir más rutas específicas de la aplicación
]
