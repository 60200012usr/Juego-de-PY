import os
import random
import tkinter as tk

CARPETA = os.path.dirname(os.path.abspath(__file__))
opciones = ["piedra", "papel", "tijera"]
EMOJIS = {"piedra": "✊", "papel": "✋", "tijera": "✌️"}

# Colores
FONDO = "#1e1e2e"
TARJETA = "#313244"
TEXTO = "#cdd6f4"
ACENTO = "#89b4fa"

ventana = tk.Tk()
ventana.title("Piedra, papel o tijera")
ventana.geometry("460x520")
ventana.config(bg=FONDO)

# Cargar imágenes (piedra.png, papel.png, tijera.png) si existen en la misma carpeta
imagenes = {}
for op in opciones:
    ruta = os.path.join(CARPETA, f"{op}.png")
    if os.path.exists(ruta):
        try:
            imagenes[op] = tk.PhotoImage(file=ruta)
        except tk.TclError:
            pass  # si falla, se usará el emoji


def mostrar(label, op):
    """Muestra la imagen de la opción (o su emoji si no hay imagen)."""
    if op in imagenes:
        label.config(image=imagenes[op], text="")
    else:
        label.config(image="", text=EMOJIS[op])


def jugar(jugador):
    computadora = random.choice(opciones)

    if jugador == computadora:
        resultado, color = "¡Empate!", "#f9e2af"
    elif (jugador == "piedra" and computadora == "tijera") or \
         (jugador == "papel" and computadora == "piedra") or \
         (jugador == "tijera" and computadora == "papel"):
        resultado, color = "¡Ganaste! 🎉", "#a6e3a1"
    else:
        resultado, color = "Perdiste", "#f38ba8"

    mostrar(img_jugador, jugador)
    mostrar(img_compu, computadora)
    label_resultado.config(text=resultado, fg=color)

    for b in botones:
        b.config(state="disabled")
    label_pregunta.pack(pady=(15, 5))
    frame_final.pack()


def reiniciar():
    for lbl in (img_jugador, img_compu):
        lbl.config(image="", text="?")
    label_resultado.config(text="Elige una opción", fg=TEXTO)
    for b in botones:
        b.config(state="normal")
    label_pregunta.pack_forget()
    frame_final.pack_forget()


# --- Título ---
tk.Label(ventana, text="Piedra, papel o tijera", font=("Arial", 18, "bold"),
         bg=FONDO, fg=ACENTO).pack(pady=15)

# --- Zona del duelo ---
frame_duelo = tk.Frame(ventana, bg=FONDO)
frame_duelo.pack()

col_j = tk.Frame(frame_duelo, bg=TARJETA, width=140, height=140)
col_j.grid(row=0, column=0, padx=10)
col_j.pack_propagate(False)
img_jugador = tk.Label(col_j, text="?", font=("Arial", 50), bg=TARJETA, fg=TEXTO)
img_jugador.pack(expand=True)
tk.Label(frame_duelo, text="Tú", bg=FONDO, fg=TEXTO).grid(row=1, column=0)

tk.Label(frame_duelo, text="VS", font=("Arial", 14, "bold"),
         bg=FONDO, fg=TEXTO).grid(row=0, column=1)

col_c = tk.Frame(frame_duelo, bg=TARJETA, width=140, height=140)
col_c.grid(row=0, column=2, padx=10)
col_c.pack_propagate(False)
img_compu = tk.Label(col_c, text="?", font=("Arial", 50), bg=TARJETA, fg=TEXTO)
img_compu.pack(expand=True)
tk.Label(frame_duelo, text="Computadora", bg=FONDO, fg=TEXTO).grid(row=1, column=2)

label_resultado = tk.Label(ventana, text="Elige una opción", font=("Arial", 16, "bold"),
                           bg=FONDO, fg=TEXTO)
label_resultado.pack(pady=20)

# --- Botones de opciones ---
frame_opciones = tk.Frame(ventana, bg=FONDO)
frame_opciones.pack()

botones = []
for op in opciones:
    if op in imagenes:
        b = tk.Button(frame_opciones, image=imagenes[op], text=op.capitalize(),
                      compound="top", bg=TARJETA, fg=TEXTO, activebackground=ACENTO,
                      relief="flat", padx=10, pady=8, command=lambda o=op: jugar(o))
    else:
        b = tk.Button(frame_opciones, text=f"{EMOJIS[op]}\n{op.capitalize()}",
                      font=("Arial", 14), width=7, bg=TARJETA, fg=TEXTO,
                      activebackground=ACENTO, relief="flat",
                      command=lambda o=op: jugar(o))
    b.pack(side="left", padx=6)
    botones.append(b)

# --- Jugar de nuevo ---
label_pregunta = tk.Label(ventana, text="¿Quieres jugar de nuevo?",
                          font=("Arial", 12), bg=FONDO, fg=TEXTO)

frame_final = tk.Frame(ventana, bg=FONDO)
tk.Button(frame_final, text="Sí", width=8, bg="#a6e3a1", relief="flat",
          command=reiniciar).pack(side="left", padx=5)
tk.Button(frame_final, text="No", width=8, bg="#f38ba8", relief="flat",
          command=ventana.destroy).pack(side="left", padx=5)

ventana.mainloop()