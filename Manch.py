import random

opciones = ["piedra", "papel", "tijera"]

jugador = input("Elige piedra, papel o tijera: ").lower().strip()

if jugador not in opciones:
    print("Opción no válida.")
else:
    computadora = random.choice(opciones)
    print(f"La computadora eligió: {computadora}")

    if jugador == computadora:
        print("¡Empate!")
    elif (jugador == "piedra" and computadora == "tijera") or \
         (jugador == "papel" and computadora == "piedra") or \
         (jugador == "tijera" and computadora == "papel"):
        print("¡Ganaste! 🎉")
    else:
        print("Perdiste.")