import cv2 as cv
import numpy as np
import easyocr
import os

# Rutas
ruta_cartas = "/Users/danieledenwynter/Desktop/BlackjackScanner/Cartas"
ruta_palos = "/Users/danieledenwynter/Desktop/BlackjackScanner/Palos"
ruta_guardado = "/Users/danieledenwynter/Desktop/BlackjackScanner/CartasProcesadas"

# Crear carpeta si no existe
os.makedirs(ruta_guardado, exist_ok=True)

# OCR
reader = easyocr.Reader(["en"], gpu=False)

# Cargar plantillas con canal alfa si lo tienen
def cargar_gris_sin_fondo(path):
    img = cv.imread(path, cv.IMREAD_UNCHANGED)
    if img.shape[2] == 4:
        alpha = img[:, :, 3]
        gray = cv.cvtColor(img[:, :, :3], cv.COLOR_BGR2GRAY)
        gray[alpha == 0] = 255
        return gray
    else:
        return cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Plantillas
plantillas_negros = {
    "Picas ♠": cargar_gris_sin_fondo(f"{ruta_palos}/picas.png"),
    "Treboles ♣": cargar_gris_sin_fondo(f"{ruta_palos}/trebol.png")
}
plantillas_rojos = {
    "Corazones ♥": cargar_gris_sin_fondo(f"{ruta_palos}/corazon.png"),
    "Diamantes ♦": cargar_gris_sin_fondo(f"{ruta_palos}/diamante.png")
}

# Procesar cartas
for archivo in os.listdir(ruta_cartas):
    if not archivo.lower().endswith((".jpg", ".png", ".jpeg")):
        continue

    path = os.path.join(ruta_cartas, archivo)
    print(f"\n🃏 Procesando: {archivo}")
    
    img = cv.imread(path)
    img_copy = img.copy()
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # OCR del número
    numero_detectado = "¿?"
    ocr_results = reader.readtext(img, paragraph=False)
    for result in ocr_results:
        text = result[1]
        numero_detectado = text
        (top_left, _, _, _) = result[0]
        x, y = map(int, top_left)
        cv.putText(img_copy, f"#{text}", (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 255), 2)
        break

    # Crear máscaras por color
    lower_black = np.array([0, 0, 0])
    upper_black = np.array([180, 255, 50])
    mask_black = cv.inRange(hsv, lower_black, upper_black)

    lower_red1 = np.array([0, 100, 100])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([160, 100, 100])
    upper_red2 = np.array([179, 255, 255])
    mask_red1 = cv.inRange(hsv, lower_red1, upper_red1)
    mask_red2 = cv.inRange(hsv, lower_red2, upper_red2)
    mask_red = cv.bitwise_or(mask_red1, mask_red2)

    mejor_palo = None
    mejor_valor = -1
    coord_palo = None

    # Buscar símbolos en zonas rojas y negras
    for mask, plantillas in [(mask_black, plantillas_negros), (mask_red, plantillas_rojos)]:
        contornos, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        for cnt in contornos:
            x, y, w, h = cv.boundingRect(cnt)
            if 25 < w < 100 and 25 < h < 100:
                roi_gray = gray[y:y+h, x:x+w]
                for nombre, plantilla in plantillas.items():
                    plantilla_resized = cv.resize(plantilla, (w, h))
                    resultado = cv.matchTemplate(roi_gray, plantilla_resized, cv.TM_CCOEFF_NORMED)
                    _, max_val, _, _ = cv.minMaxLoc(resultado)
                    if max_val > mejor_valor:
                        mejor_valor = max_val
                        mejor_palo = nombre
                        coord_palo = (x, y + h + 20)

    # Dibujar resultado
    if mejor_valor >= 0.5:
        print(f"✅ Número: {numero_detectado} | Palo: {mejor_palo} (confianza: {mejor_valor:.2f})")
        if coord_palo:
            cv.putText(img_copy, mejor_palo, coord_palo, cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)
    else:
        print(f"⚠️ Número: {numero_detectado} | Palo: No detectado (confianza: {mejor_valor:.2f})")

    # Guardar imagen procesada
    salida = os.path.join(ruta_guardado, f"procesada_{archivo}")
    cv.imwrite(salida, img_copy)
    print(f"📸 Imagen guardada en: {salida}")

    # Mostrar imagen
    cv.imshow("Carta Detectada", img_copy)
    print("Presiona una tecla para continuar...")
    cv.waitKey(0)
    cv.destroyAllWindows()
