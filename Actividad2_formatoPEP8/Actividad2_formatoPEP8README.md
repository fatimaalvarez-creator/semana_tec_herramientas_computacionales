# Actividad 2. Filtrado de la imagen en formato PEP8 y agregando commits
 Herramientas computacionales: el arte de la programación (Gpo 201) - TC1001S.201 <br/>
 Fátima Álvarez Nuño - A01645815 <br/>
 Fecha: 06/05/2025 <br/>

## Objetivo
Este proyecto realiza el procesamiento de una imagen para detectar texto presente en ella utilizando técnicas de visión por computadora y OCR (Reconocimiento Óptico de Caracteres). Para ello, se emplean bibliotecas como OpenCV, EasyOCR y Matplotlib.

## Descripción de lo realizado
 El flujo del código incluye los siguientes pasos:

1. **Carga de imagen**: Se lee una imagen de una placa vehicular (`placa3.jpg`) con OpenCV.
2. **Conversión de color**: Se convierte la imagen de BGR a RGB para su visualización con Matplotlib.
3. **Escala de grises**: Se transforma la imagen a escala de grises para facilitar el procesamiento.
4. **Suavizado**: Se aplica un filtro Gaussiano para reducir el ruido.
5. **Detección de bordes**: Se detectan bordes con el algoritmo de Canny.
6. **OCR con EasyOCR**: Se utiliza EasyOCR para detectar y extraer textos de la imagen en español e inglés.
7. **Visualización**: Se muestran cuatro imágenes:
   - Imagen original (RGB)
   - Imagen en escala de grises
   - Imagen con bordes detectados
   - Imagen con los textos detectados por OCR marcados con recuadros verdes
8. **Salida en consola**: Se imprimen los textos detectados.

## Requisitos importantes
Instalar las dependencias necesarias con:

```bash
pip install opencv-python easyocr matplotlib numpy
