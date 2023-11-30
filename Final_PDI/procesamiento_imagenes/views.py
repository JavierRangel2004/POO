import matplotlib
import os
import numpy as np
import cv2 as cv
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render
# Debe ir antes de importar pyplot o cualquier otro componente de Matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
from PIL import Image


def assure_rgb(imagen):
    """
    Asegura que la imagen esté en espacio de color RGB. OpenCV carga imágenes en BGR por defecto.
    """
    if imagen.ndim == 3 and imagen.shape[2] == 3:  # Verifica si la imagen tiene 3 canales
        return cv.cvtColor(imagen, cv.COLOR_BGR2RGB)
    return imagen


def reducir_ruido(imagen):
    """
    Reduce el ruido de una imagen utilizando un filtro bilateral.

    Args:
    imagen (np.ndarray): Imagen de entrada en formato de matriz numpy.

    Returns:
    np.ndarray: Imagen con ruido reducido.
    """
    imagen_rgb = assure_rgb(imagen)
    imagen_sin_ruido = cv.bilateralFilter(imagen_rgb, 9, 75, 75)
    return imagen_sin_ruido


def aplicar_filtro_sepia(imagen):
    """
    Aplica un filtro sepia a una imagen.

    Args:
    imagen (np.ndarray): Imagen de entrada en formato de matriz numpy.

    Returns:
    np.ndarray: Imagen con filtro sepia.
    """
    imagen_rgb = assure_rgb(imagen)
    imagen_sepia = np.dot(imagen_rgb, [[0.272, 0.534, 0.131],
                                       [0.349, 0.686, 0.168],
                                       [0.393, 0.769, 0.189]])
    imagen_sepia = np.clip(imagen_sepia, 0, 255)
    imagen_sepia = imagen_sepia.astype('uint8')
    return imagen_sepia


def mejorar_calidad(imagen):
    """
    Mejora la calidad de una imagen aumentando su nitidez.
    """
    imagen_rgb = assure_rgb(imagen)
    kernel = np.array([[-1, -1, -1],
                       [-1, 9, -1],
                       [-1, -1, -1]])
    imagen_mejorada = cv.filter2D(imagen_rgb, -1, kernel)
    return imagen_mejorada


def convertir_a_bnw(imagen):
    """
    Convierte una imagen a blanco y negro.
    """
    imagen_rgb = assure_rgb(imagen)
    imagen_bnw = cv.cvtColor(imagen_rgb, cv.COLOR_RGB2GRAY)
    return imagen_bnw


def convertir_a_BGR(imagen):
    """
    Convierte una imagen de formato RGB a BGR.
    """
    imagen = assure_rgb(imagen)
    imagen_BGR = cv.cvtColor(imagen, cv.COLOR_RGB2BGR)
    return imagen_BGR


def binarizar_imagen(imagen, umbral=127):
    """
    Binariza una imagen utilizando un umbral.

    Args:
    imagen (np.ndarray): Imagen de entrada en formato de matriz numpy.
    umbral (int): Umbral para la binarización. Valor por defecto es 127.

    Returns:
    np.ndarray: Imagen binarizada.
    """
    imagen_rgb = assure_rgb(imagen)
    _, imagen_binarizada = cv.threshold(cv.cvtColor(
        imagen_rgb, cv.COLOR_RGB2GRAY), umbral, 255, cv.THRESH_BINARY)
    return imagen_binarizada


def negativo_imagen(imagen):
    """
    Crea el negativo de una imagen.

    Args:
    imagen (np.ndarray): Imagen de entrada en formato de matriz numpy.

    Returns:
    np.ndarray: Negativo de la imagen.
    """
    imagen_rgb = assure_rgb(imagen)
    imagen_negativa = 255 - imagen_rgb
    return imagen_negativa


def transformacion_logaritmica(imagen, constante=1):
    """
    Aplica una transformación logarítmica a la imagen.

    Args:
    imagen (np.ndarray): Imagen de entrada en formato de matriz numpy.
    constante (float): Constante para ajustar la transformación. Valor por defecto es 1.

    Returns:
    np.ndarray: Imagen con transformación logarítmica.
    """
    imagen_rgb = assure_rgb(imagen)
    c = constante * 255 / np.log(1 + np.max(imagen_rgb))
    imagen_log = c * np.log(1 + imagen_rgb)
    imagen_log = np.array(imagen_log, dtype=np.uint8)
    return imagen_log


def histograma_imagen(imagen):
    """
    Calcula y muestra el histograma combinado de los canales RGB de una imagen.

    Args:
    imagen (np.ndarray): Imagen de entrada en formato de matriz numpy.

    Returns:
    np.ndarray: Imagen de los histogramas combinados.
    """
    imagen_rgb = assure_rgb(imagen)
    colores = ('r', 'g', 'b')

    # Crear un histograma para cada canal de color
    for i, color in enumerate(colores):
        hist = cv.calcHist([imagen_rgb], [i], None, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])

    # Guardar el histograma en un buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)

    # Cargar la imagen del buffer y convertirla en un array de numpy
    imagen_histograma = np.array(Image.open(buf))
    buf.close()

    # Cerrar la figura de Matplotlib para liberar memoria
    plt.close()

    return imagen_histograma


def filtrar_suavizar_imagen(imagen, kernel_size=5):
    """
    Suaviza una imagen utilizando un filtro Gaussiano.

    Args:
    imagen (np.ndarray): Imagen de entrada en formato de matriz numpy.
    kernel_size (int): Tamaño del kernel para el filtro. Valor por defecto es 5.

    Returns:
    np.ndarray: Imagen suavizada.
    """
    imagen_rgb = assure_rgb(imagen)
    imagen_suavizada = cv.GaussianBlur(
        imagen_rgb, (kernel_size, kernel_size), 0)
    return imagen_suavizada


def umbralizacion_adaptativa(imagen, max_value=255, block_size=11, C=2):
    """
    Aplica umbralización adaptativa a una imagen.

    Args:
    imagen (np.ndarray): Imagen de entrada en formato de matriz numpy.
    max_value (int): Valor máximo a utilizar en la umbralización. Valor por defecto es 255.
    block_size (int): Tamaño del bloque para calcular el umbral. Valor por defecto es 11.
    C (int): Constante a restar del promedio o suma ponderada. Valor por defecto es 2.

    Returns:
    np.ndarray: Imagen con umbralización adaptativa.
    """
    imagen_rgb = assure_rgb(imagen)
    imagen_gris = cv.cvtColor(imagen_rgb, cv.COLOR_RGB2GRAY)
    imagen_umbralizada = cv.adaptiveThreshold(
        imagen_gris, max_value, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, block_size, C)
    return imagen_umbralizada


def image_upload_view(request):
    if request.method == 'POST':
        uploaded_image = request.FILES.get('image_file', None)

        if uploaded_image:
            fs = FileSystemStorage()
            file_name = fs.save(uploaded_image.name, uploaded_image)
            file_url = fs.url(file_name)

            # Load the image using OpenCV
            image_path = fs.path(file_name)

            if os.path.exists(image_path):
                image = cv.imread(image_path)

                if image is None:
                    return HttpResponse("Error al leer la imagen.")

                try:
                    image_sin_ruido = reducir_ruido(image)
                    image_mejorada = mejorar_calidad(image)
                    image_sepia = aplicar_filtro_sepia(image)
                    image_BGR = convertir_a_BGR(image)
                    image_bnw = convertir_a_bnw(image)
                    image_binarizada = binarizar_imagen(image)
                    image_negativa = negativo_imagen(image)
                    image_log = transformacion_logaritmica(image)
                    # Needs additional processing to display
                    image_histograma = histograma_imagen(image)
                    image_suavizada = filtrar_suavizar_imagen(image)
                    image_umbralizada = umbralizacion_adaptativa(image)

                    filters = {
                        'original': file_url,
                        'sin_ruido': save_filter_image(fs, image_sin_ruido, 'sin_ruido_' + file_name),
                        'mejorada': save_filter_image(fs, image_mejorada, 'mejorada_' + file_name),
                        'sepia': save_filter_image(fs, image_sepia, 'sepia_' + file_name),
                        'BGR': save_filter_image(fs, image_BGR, 'BGR_' + file_name),
                        'bnw': save_filter_image(fs, image_bnw, 'bnw_' + file_name),
                        'binarizada': save_filter_image(fs, image_binarizada, 'binarizada_' + file_name),
                        'negativa': save_filter_image(fs, image_negativa, 'negativa_' + file_name),
                        'log': save_filter_image(fs, image_log, 'log_' + file_name),
                        # Needs additional processing
                        'histograma': save_filter_image(fs, image_histograma, 'histograma_' + file_name),
                        'suavizada': save_filter_image(fs, image_suavizada, 'suavizada_' + file_name),
                        'umbralizada': save_filter_image(fs, image_umbralizada, 'umbralizada_' + file_name),
                    }
                    return render(request, 'procesamiento_imagenes/show_image.html', filters)

                except Exception as e:
                    return HttpResponse(f"Error durante el procesamiento de la imagen: {e}")

            else:
                return HttpResponse("El archivo de imagen no se encuentra en el servidor.")

        else:
            return HttpResponse("No se cargó ningún archivo.")

    return render(request, 'procesamiento_imagenes/upload_image.html')


def save_filter_image(file_storage, image, file_name):
    """
    Save a processed image and return its URL.
    """
    # Convert from BGR to RGB if necessary (OpenCV uses BGR by default)
    # Check if the image has 3 channels
    if image.ndim == 3 and image.shape[2] == 3:
        image = cv.cvtColor(image, cv.COLOR_BGR2RGB)

    # Save the image to a temporary file
    temp_file = file_storage.path(file_name)
    cv.imwrite(temp_file, image)

    # Return the URL to access the image
    return file_storage.url(file_name)
