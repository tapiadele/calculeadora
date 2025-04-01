import tkinter as tk
from tkinter import messagebox
import re

def calcular_expresion(expresion):
    try:
        tokens = re.findall(r'\d+\.\d+|\d+|[+\-*/]', expresion)
        
        i = 0
        while i < len(tokens):
            if tokens[i] in ('*', '/'):  
                if tokens[i] == '*':
                    resultado = float(tokens[i-1]) * float(tokens[i+1])
                else:
                    if float(tokens[i+1]) == 0:
                        return "Error: División por cero"
                    resultado = float(tokens[i-1]) / float(tokens[i+1])
                
                tokens[i-1:i+2] = [str(resultado)]
                i -= 1
            i += 1
        
        resultado = float(tokens[0])
        i = 1
        while i < len(tokens):
            if tokens[i] == '+':
                resultado += float(tokens[i+1])
            elif tokens[i] == '-':
                resultado -= float(tokens[i+1])
            i += 2
        
        return resultado
    except Exception as e:
        return "Error en la expresión"

def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        expresion = entry_var.get()
        resultado = calcular_expresion(expresion)
        entry_var.set(resultado)
    elif text == "C":
        entry_var.set("")
    elif text == "⌫":
        entry_var.set(entry_var.get()[:-1])
    else:
        entry_var.set(entry_var.get() + text)

root = tk.Tk()
root.title("Calculadora Picante")

entry_var = tk.StringVar()
entry = tk.Entry(root, textvar=entry_var, font="Arial 20", justify="right")
entry.pack(fill="both", ipadx=8, padx=10, pady=10)

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"],
    ["⌫"]
]

frame = tk.Frame(root)
frame.pack()

for row in buttons:
    row_frame = tk.Frame(frame)
    row_frame.pack(side="top")
    for btn_text in row:
        btn = tk.Button(row_frame, text=btn_text, font="Arial 20", width=5, height=2)
        btn.pack(side="left", padx=5, pady=5)
        btn.bind("<Button-1>", on_click)

root.mainloop()