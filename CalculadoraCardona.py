import tkinter as tk
from tkinter import messagebox

class Operaciones:
    def __init__(self, a, b):  # Corregido de _init_ a __init__
        self.a = float(a)
        self.b = float(b)

    def sumar(self):
        return self.a + self.b
    
    def restar(self):
        return self.a - self.b
    
    def multiplicar(self):
        return self.a * self.b
    
    def dividir(self):
        if self.b == 0:
            return "No se puede dividir entre cero"
        return self.a / self.b

def calcular(operador):
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        operacion = Operaciones(a, b)

        if operador == "+":
            resultado = operacion.sumar()
        elif operador == "-":
            resultado = operacion.restar()
        elif operador == "*":
            resultado = operacion.multiplicar()
        elif operador == "/":
            resultado = operacion.dividir()
        else:
            resultado = "Operación no válida"

        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos.")

# Ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("300x250")  # Ajustado para una mejor visualización

# Entradas
tk.Label(ventana, text="Primer número:").pack(pady=5)
entry1 = tk.Entry(ventana, justify='center')
entry1.pack(pady=5)

tk.Label(ventana, text="Segundo número:").pack(pady=5)
entry2 = tk.Entry(ventana, justify='center')
entry2.pack(pady=5)

# Frame para botones de operaciones
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

tk.Button(frame_botones, text="+", width=5, command=lambda: calcular("+")).grid(row=0, column=0, padx=5)
tk.Button(frame_botones, text="-", width=5, command=lambda: calcular("-")).grid(row=0, column=1, padx=5)
tk.Button(frame_botones, text="*", width=5, command=lambda: calcular("*")).grid(row=0, column=2, padx=5)
tk.Button(frame_botones, text="/", width=5, command=lambda: calcular("/")).grid(row=0, column=3, padx=5)

# Resultado
label_resultado = tk.Label(ventana, text="Resultado: ", font=("Arial", 12, "bold"))
label_resultado.pack(pady=10)

ventana.mainloop()
