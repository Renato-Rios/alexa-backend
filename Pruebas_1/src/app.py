import tkinter as tk
import subprocess

def alexa_hablar(texto):
    subprocess.run([
        "bash",
        "../alexa/alexa_remote_control.sh",
        "-e",
        f'speak:"{texto}"'
    ])

def saludar():
    alexa_hablar("Hola, intenta decir hola")

def felicitar():
    alexa_hablar("Muy bien, lo hiciste excelente")

def intentar():
    alexa_hablar("Intenta otra vez, tu puedes")

# Crear ventana
ventana = tk.Tk()
ventana.title("Asistente Terapéutico")
ventana.geometry("400x300")

# Título
label = tk.Label(ventana, text="Control Alexa", font=("Arial", 16))
label.pack(pady=10)

# Botones
btn_saludo = tk.Button(ventana, text="Saludar", command=saludar, width=20)
btn_saludo.pack(pady=5)

btn_felicitar = tk.Button(ventana, text="Felicitar", command=felicitar, width=20)
btn_felicitar.pack(pady=5)

btn_intentar = tk.Button(ventana, text="Intentar", command=intentar, width=20)
btn_intentar.pack(pady=5)

# Ejecutar app
ventana.mainloop()