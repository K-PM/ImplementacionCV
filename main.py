import cv2
import numpy as np

imagen = cv2.imread('imagen3.jpg')

# Convertir la imagen a los diferentes espacios de color
imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
imagen_yiq = cv2.cvtColor(imagen, cv2.COLOR_BGR2YCrCb)
imagen_cmy = cv2.cvtColor(imagen, cv2.COLOR_BGR2YUV)
imagen_ycbcr = cv2.cvtColor(imagen, cv2.COLOR_BGR2YCrCb)
imagen_hsi = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

resolucion_dpi = 200  # resolución de la imagen
resolucion_ppcm = resolucion_dpi / 2.54

size_pixels = (int(3 * resolucion_ppcm), int(3 * resolucion_ppcm))
imagen_rgb_resized = cv2.resize(imagen_rgb, size_pixels)
imagen_yiq_resized = cv2.resize(imagen_yiq, size_pixels)
imagen_cmy_resized = cv2.resize(imagen_cmy, size_pixels)
imagen_ycbcr_resized = cv2.resize(imagen_ycbcr, size_pixels)
imagen_hsi_resized = cv2.resize(imagen_hsi, size_pixels)

imagenes_concatenadas_horizontal = cv2.hconcat([imagen_rgb_resized, imagen_yiq_resized, imagen_cmy_resized, imagen_ycbcr_resized, imagen_hsi_resized])
titulos = ['RGB', 'YIQ', 'CMY', 'YCbCr', 'HSI']
font = cv2.FONT_HERSHEY_SIMPLEX
for i, titulo in enumerate(titulos):
    cv2.putText(imagenes_concatenadas_horizontal, titulo, (i * size_pixels[0] + 20, altura - 10), font, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

cv2.imshow('Imagenes', imagenes_concatenadas_horizontal)
cv2.waitKey(0)
cv2.destroyAllWindows()
