# Importar librerías necesarias
import os
import cv2 as cv

# Ruta donde están las cartas procesadas
ruta_cartas = "corazon.png"

# Valores de las cartas
def valor_carta(texto):
    texto = texto.strip().upper()
    if texto == "A":
        return 11
    elif texto in ["J", "Q", "K"]:
        return 10
    elif texto == "10":
        return 10
    else:
        try:
            return int(texto)
        except:
            return 0

# Ajustar As si se pasa de 21
def ajustar_ases(mano):
    total = sum(mano)
    ases = mano.count(11)
    while total > 21 and ases:
        total -= 10
        ases -= 1
    return total

# Simular juego
def jugar_blackjack():
    cartas = sorted([f for f in os.listdir(ruta_cartas) if f.startswith("procesada_")])
    print("🃏 Bienvenido al Blackjack con tus cartas escaneadas!\n")
    print("Cartas disponibles:", len(cartas))

    indice = 0
    mano = []

    while indice < len(cartas):
        archivo = cartas[indice]
        path = os.path.join(ruta_cartas, archivo)
        print(f"\n📸 Carta: {archivo}")
        img = cv.imread(path)
        cv.imshow("Tu carta", img)
        cv.waitKey(1000)  # Mostrarla 1 segundo
        cv.destroyAllWindows()

        # Obtener valor desde nombre del archivo (ej. procesada_10diamante.jpg → "10")
        nombre = archivo.replace("procesada_", "").split(".")[0]
        valor_detectado = ''.join(filter(str.isalnum, nombre.upper()))  # Ej: "10DIAMANTE"

        # Buscar primero si contiene "10", luego una sola letra o número
        valor = 0
        if "10" in valor_detectado:
            valor = 10
        else:
            for char in valor_detectado:
                if char in "A23456789JQK":
                    valor = valor_carta(char)
                    break

        if valor == 0:
            print("⚠️ No se pudo detectar valor, se salta esta carta.")
            indice += 1
            continue

        mano.append(valor)
        total = ajustar_ases(mano)
        print(f"🧮 Total actual: {total}")

        if total > 21:
            print("💥 Te pasaste. ¡Perdiste!")
            return

        if total == 21:
            print("🎉 ¡21 exactos! ¡Ganaste!")
            return

        accion = input("¿Quieres otra carta? (s = sí / n = no): ").strip().lower()
        if accion != "s":
            print(f"\n🛑 Te plantaste con: {total}")
            return

        indice += 1

    print(f"\n🃏 Te quedaste sin cartas. Total final: {ajustar_ases(mano)}")

# Ejecutar juego
if __name__ == "__main__":
    jugar_blackjack()
