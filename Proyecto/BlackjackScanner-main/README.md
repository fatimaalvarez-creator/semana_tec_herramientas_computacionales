# 🃏 BlackjackScan  
## Herramientas Computacionales: El Arte de la Programación (Gpo 201) - TC1001S.201  
### Fátima Álvarez Nuño - A01645815  
### Daniel Eden Wynter González - A01645202  

---

## 🎯 Objetivo
Este proyecto permite escanear imágenes de cartas físicas de blackjack, detectar su número y palo usando OCR (reconocimiento óptico de caracteres), y luego simular una partida de blackjack interactiva con esas cartas.

---

## 📝 Descripción

El sistema consta de dos partes:
1. **Procesamiento de cartas:** Detecta el número y el palo de cada carta mediante EasyOCR y plantillas.
2. **Simulación de juego:** Usa las cartas detectadas para simular una partida de blackjack.

---

## ⚙️ Requisitos

- Python 3.7+
- OpenCV
- NumPy
- EasyOCR
- Imágenes de cartas con fondo blanco o neutro

---

## 🛠 Instalación
Instala los módulos necesarios con:
```bash
pip install opencv-python numpy easyocr
```

## ▶️ Como ejecutar
Ejecuta el script de escaneo:
```bash
python CardScanner.py
```

Luego, ejecuta el simulador de blackjack:
```bash
python blackjackscan_juego.py
```

## 🔍 Funcionalidad
* Detecta el número usando EasyOCR.
* Detecta el palo mediante matchTemplate y máscaras de color HSV.
* Etiqueta las cartas y las guarda en CartasProcesadas/
* Simula una partida donde el jugador puede decidir si pedir más cartas o plantarse.

## 🚀 Mejoras Futuras
* Captura desde cámara en tiempo real
* Captura optimizada en tiempo real desde cámara.
* Mayor precisión en reconocimiento de texto y símbolos.
* Implementación de una interfaz gráfica interactiva.
