import random
import tkinter as tk

opciones = ["piedra", "papel", "tijera"]


def jugar(jugador):
    computadora = random.choice(opciones)

    if jugador == computadora:
        resultado = "¡Empate!"
    elif (jugador == "piedra" and computadora == "tijera") or \
         (jugador == "papel" and computadora == "piedra") or \
         (jugador == "tijera" and computadora == "papel"):
        resultado = "¡Ganaste! 🎉"
    else:
        resultado = "Perdiste."

    label_resultado.config(
        text=f"Tú: {jugador}\nComputadora: {computadora}\n\n{resultado}"
    )

    # Desactivar opciones y mostrar la pregunta de jugar de nuevo
    for b in botones:
        b.config(state="disabled")
    label_pregunta.pack(pady=5)
    frame_final.pack()


def reiniciar():
    label_resultado.config(text="Elige una opción:")
    for b in botones:
        b.config(state="normal")
    label_pregunta.pack_forget()
    frame_final.pack_forget()


ventana = tk.Tk()
ventana.title("Piedra, papel o tijera")
ventana.geometry("340x320")

label_resultado = tk.Label(ventana, text="Elige una opción:", font=("Arial", 13))
label_resultado.pack(pady=15)

frame_opciones = tk.Frame(ventana)
frame_opciones.pack()

botones = []
for op in opciones:
    b = tk.Button(frame_opciones, text=op.capitalize(), width=9,
                  command=lambda o=op: jugar(o))
    b.pack(side="left", padx=5)
    botones.append(b)

label_pregunta = tk.Label(ventana, text="¿Quieres jugar de nuevo?", font=("Arial", 11))

frame_final = tk.Frame(ventana)
tk.Button(frame_final, text="Sí", width=8, command=reiniciar).pack(side="left", padx=5)
tk.Button(frame_final, text="No", width=8, command=ventana.destroy).pack(side="left", padx=5)

ventana.mainloop()