import tkinter as tk
from tkinter import messagebox
import random

def verificar_numero():
    global numero_secreto, intentos
    try:
        intento = int(entrada.get())
    except ValueError:
        resultado.config(text="¡Ingresa un número válido!")
        return

    intentos += 1
    intentos_restantes.config(text=f"Intentos restantes: {8 - intentos}")

    if intento < numero_secreto:
        resultado.config(text="¡Demasiado bajo!")
    elif intento > numero_secreto:
        resultado.config(text="¡Demasiado alto!")
    else:
        resultado.config(text="¡Adivinaste! Era el " + str(numero_secreto))
        messagebox.showinfo("¡Felicidades!", "¡Adivinaste el número!")
        reiniciar_juego()

    if intentos == 8:
        resultado.config(text="¡Game Over!")
        if messagebox.askyesno("Game Over", "¿Quieres volver a intentar?"):
            reiniciar_juego()
        else:
            ventana.destroy()

def generar_numero():
    global numero_secreto, intentos
    numero_secreto = random.randint(1, 100)
    intentos = 0
    resultado.config(text="He pensado un número entre 1 y 100. ¡Adivínalo!")
    intentos_restantes.config(text=f"Intentos restantes: {8 - intentos}")
    entrada.delete(0, tk.END)  # Limpiar el campo de entrada

def reiniciar_juego():
    generar_numero()
    entrada.delete(0, tk.END)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Adivina el número")

# Crear los widgets
etiqueta = tk.Label(ventana, text="¡Adivina el número!")
etiqueta.pack(pady=10)

entrada = tk.Entry(ventana)
entrada.pack(pady=10)

boton = tk.Button(ventana, text="Verificar", command=verificar_numero)
boton.pack(pady=10)

resultado = tk.Label(ventana, text="")
resultado.pack(pady=10)

intentos_restantes = tk.Label(ventana, text="")
intentos_restantes.pack()

# Generar el primer número secreto
generar_numero()

# Iniciar el bucle principal de la aplicación
ventana.mainloop()