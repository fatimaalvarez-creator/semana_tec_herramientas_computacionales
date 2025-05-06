# Importar las bibliotecas necesarias
import cv2
import numpy as np
import matplotlib.pyplot as plt
import easyocr

# Cargar la imagen y convertir a RGB
imagen = cv2.imread("placa3.jpg")
imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

# Convertir a escala de grises
imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Aplicar filtro Gaussiano para suavizar la imagen
imagen_suavizada = cv2.GaussianBlur(imagen_gris, (5, 5), 0)

# Detectar bordes con el algoritmo de Canny
bordes = cv2.Canny(imagen_suavizada, 100, 200)

# Inicializar el lector OCR con soporte en español e inglés
lector = easyocr.Reader(['es', 'en'])
resultados_ocr = lector.readtext(imagen)

# Dibujar los textos detectados sobre una copia de la imagen
imagen_ocr = imagen_rgb.copy()
for bbox, texto, confianza in resultados_ocr:
    (tl, tr, br, bl) = bbox
    punto_superior_izquierdo = tuple(map(int, tl))
    punto_inferior_derecho = tuple(map(int, br))
    
    cv2.rectangle(imagen_ocr, punto_superior_izquierdo, punto_inferior_derecho, (0, 255, 0), 2)
    cv2.putText(imagen_ocr, texto, (punto_superior_izquierdo[0], punto_superior_izquierdo[1] - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

# Mostrar todas las imágenes procesadas
fig, axs = plt.subplots(1, 4, figsize=(20, 6))

axs[0].imshow(imagen_rgb)
axs[0].set_title('Imagen Original')
axs[0].axis('off')

axs[1].imshow(imagen_gris, cmap='gray')
axs[1].set_title('Escala de Grises')
axs[1].axis('off')

axs[2].imshow(bordes, cmap='gray')
axs[2].set_title('Bordes (Canny)')
axs[2].axis('off')

axs[3].imshow(imagen_ocr)
axs[3].set_title('OCR (EasyOCR)')
axs[3].axis('off')

plt.tight_layout()
plt.show()

# Imprimir los textos detectados en consola
print("\nTextos detectados:")
for _, texto, _ in resultados_ocr:
    print(f"Texto: '{texto}'")