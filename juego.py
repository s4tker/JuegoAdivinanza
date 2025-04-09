import random

def JuegoAdivinanza():
    """JUEGO PARA ADIVINAR UN NÚMERO ALEATORIO"""

    NumSecreto = random.randint(1, 100)
    intentos = 0

    print("BIENVENIDO AL JUEGO DE ADIVINANZA\n")
    print("Estoy pensando en un número entre el 1 y 100.")
    print("Te deseo mucha suerte, ¡aunque a veces este juego puede ser un poco frustrante si el número se resiste!\n")

    while True:
        try:
            intento = int(input("Adivina el número: "))
            intentos += 1

            if intento < NumSecreto:
                print("Demasiado Bajo. ¡Intenta de nuevo!")
                print("")

            elif intento > NumSecreto:
                print("Demasiado alto. ¡Intenta de nuevo!")
                print("")

            else:
                print(f"¡Felicidades! Adivinaste el número {NumSecreto} en {intentos} intentos.")
                print("")
                break

        except ValueError:
            print("Por favor, ingresa un número entero Válido.\n")
            print("")
            
if __name__ == "__main__":
    JuegoAdivinanza()
