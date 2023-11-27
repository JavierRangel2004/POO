from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import cv2 as cv
import numpy as np
import os


def assure_rgb(imagen):
    """
    Asegura que la imagen esté en espacio de color RGB. OpenCV carga imágenes en BGR por defecto.

    Args:
    imagen (np.ndarray): Imagen de entrada en formato de matriz numpy.

    Returns:
    np.ndarray: Imagen en formato RGB.
    """
    if imagen.shape[-1] == 3:  # Solo hacer la conversión si la imagen tiene 3 canales
        return cv.cvtColor(imagen, cv.COLOR_BGR2RGB)
    return imagen


def reducir_ruido(imagen):
    """
    Reduce el ruido de una imagen utilizando un filtro de mediana.

    Args:
    imagen (np.ndarray): Imagen de entrada en formato de matriz numpy.

    Returns:
    np.ndarray: Imagen con ruido reducido.
    """
    imagen_rgb = assure_rgb(imagen)
    imagen_sin_ruido = cv.medianBlur(imagen_rgb, 5)
    return imagen_sin_ruido


def mejorar_calidad(imagen):
    """
    Mejora la calidad de una imagen aumentando su nitidez.

    Args:
    imagen (np.ndarray): Imagen de entrada en formato de matriz numpy.

    Returns:
    np.ndarray: Imagen con calidad mejorada.
    """
    imagen_rgb = assure_rgb(imagen)
    kernel = np.array([[-1, -1, -1],
                       [-1, 9, -1],
                       [-1, -1, -1]])
    imagen_mejorada = cv.filter2D(imagen_rgb, -1, kernel)
    return imagen_mejorada


def aplicar_filtro_sepia(imagen):
    """
    Aplica un filtro sepia a una imagen.

    Args:
    imagen (np.ndarray): Imagen de entrada en formato de matriz numpy.

    Returns:
    np.ndarray: Imagen con filtro sepia.
    """
    imagen_rgb = assure_rgb(imagen)
    kernel = np.array([[0.272, 0.534, 0.131],
                       [0.349, 0.686, 0.168],
                       [0.393, 0.769, 0.189]])
    imagen_sepia = cv.transform(imagen_rgb, kernel)
    return imagen_sepia


def convertir_a_bnw(imagen):
    """
    Convierte una imagen a blanco y negro.

    Args:
    imagen (np.ndarray): Imagen de entrada en formato de matriz numpy.

    Returns:
    np.ndarray: Imagen en blanco y negro.
    """
    imagen_rgb = assure_rgb(imagen)
    imagen_bnw = cv.cvtColor(imagen_rgb, cv.COLOR_RGB2GRAY)
    return imagen_bnw


def convertir_a_BGR(imagen):
    """
    Convierte una imagen de formato RGB a BGR.

    Args:
    imagen (np.ndarray): Imagen de entrada en formato de matriz numpy.

    Returns:
    np.ndarray: Imagen en formato BGR.
    """
    imagen = assure_rgb(imagen)
    imagen_BGR = cv.cvtColor(imagen, cv.COLOR_RGB2BGR)
    return imagen_BGR


def image_upload_view(request):
    if request.method == 'POST':
        uploaded_image = request.FILES.get('image_file', None)

        if uploaded_image:
            fs = FileSystemStorage()
            file_name = fs.save(uploaded_image.name, uploaded_image)
            file_url = fs.url(file_name)

            # Load the image using OpenCV
            image_path = fs.path(file_name)

            # Check if the file exists before processing
            if os.path.exists(image_path):
                image = cv.imread(image_path)

                # Check if the image was read correctly
                if image is None:
                    # Handle the case where the image is not read correctly
                    return HttpResponse("Error al leer la imagen.")

                # Apply the filters with proper error handling
                try:
                    image_sin_ruido = reducir_ruido(image)
                    image_mejorada = mejorar_calidad(image)
                    image_sepia = aplicar_filtro_sepia(image)
                    image_BGR = convertir_a_BGR(image)
                    image_bnw = convertir_a_bnw(image)
                    # ... Save and generate URLs for the processed images
                except Exception as e:
                    # Handle any other errors during processing
                    return HttpResponse(f"Error durante el procesamiento de la imagen: {e}")
                # Save the filtered images and generate URLs
                filters = {
                    'original': file_url,
                    'sin_ruido': save_filter_image(fs, image_sin_ruido, 'sin_ruido_' + file_name),
                    'mejorada': save_filter_image(fs, image_mejorada, 'mejorada_' + file_name),
                    'sepia': save_filter_image(fs, image_sepia, 'sepia_' + file_name),
                    'BGR': save_filter_image(fs, image_BGR, 'BGR_' + file_name),
                    'bnw': save_filter_image(fs, image_bnw, 'bnw_' + file_name),
                }
                return render(request, 'procesamiento_imagenes/show_image.html', filters)

            else:
                return HttpResponse("El archivo de imagen no se encuentra en el servidor.")

        else:
            return HttpResponse("No se cargó ningún archivo.")

    return render(request, 'procesamiento_imagenes/upload_image.html')


def save_filter_image(file_storage, image, file_name):
    """
    Save a processed image and return its URL.

    Args:
        file_storage (FileSystemStorage): The Django file storage system.
        image (np.ndarray): The processed image array.
        file_name (str): The name of the file to save.

    Returns:
        str: The URL of the saved image.
    """
    # Convert from BGR to RGB if necessary (OpenCV uses BGR by default)
    image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    # Save the image to a temporary file
    temp_file = file_storage.path(file_name)
    cv.imwrite(temp_file, image)
    # Return the URL to access the image
    return file_storage.url(file_name)
