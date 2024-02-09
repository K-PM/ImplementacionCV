import cv2
import numpy as np

# Cargar la imagen
imagen = cv2.imread('imagen3.jpg')

# Convertir la imagen a los diferentes espacios de color
imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
imagen_yiq = cv2.cvtColor(imagen, cv2.COLOR_BGR2YCrCb)
imagen_cmy = cv2.cvtColor(imagen, cv2.COLOR_BGR2YUV)
imagen_ycbcr = cv2.cvtColor(imagen, cv2.COLOR_BGR2YCrCb)
imagen_hsi = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

# Obtener la resolución en píxeles por centímetro
resolucion_dpi = 200  # Cambia esto según la resolución de tu imagen
resolucion_ppcm = resolucion_dpi / 2.54

# Calcular el tamaño en píxeles para 3x3 cm
size_pixels = (int(3 * resolucion_ppcm), int(3 * resolucion_ppcm))

# Cambiar el tamaño de las imágenes
imagen_rgb_resized = cv2.resize(imagen_rgb, size_pixels)
imagen_yiq_resized = cv2.resize(imagen_yiq, size_pixels)
imagen_cmy_resized = cv2.resize(imagen_cmy, size_pixels)
imagen_ycbcr_resized = cv2.resize(imagen_ycbcr, size_pixels)
imagen_hsi_resized = cv2.resize(imagen_hsi, size_pixels)

# Concatenar las imágenes horizontalmente
imagenes_concatenadas_horizontal = cv2.hconcat([imagen_rgb_resized, imagen_yiq_resized, imagen_cmy_resized, imagen_ycbcr_resized, imagen_hsi_resized])

# Agregar títulos a cada imagen
titulos = ['RGB', 'YIQ', 'CMY', 'YCbCr', 'HSI']
font = cv2.FONT_HERSHEY_SIMPLEX
altura = imagen_rgb_resized.shape[0]  # Altura de las imágenes redimensionadas
for i, titulo in enumerate(titulos):
    cv2.putText(imagenes_concatenadas_horizontal, titulo, (i * size_pixels[0] + 20, altura - 10), font, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

# Mostrar las imágenes concatenadas en una misma ventana
cv2.imshow('Imagenes', imagenes_concatenadas_horizontal)
cv2.waitKey(0)
cv2.destroyAllWindows()
