import tkinter.messagebox as mb
def mostrar_error(titulo,mensaje):
    mb.showerror(titulo,mensaje)
def mostrar_tutorial():
    mensaje = (
    "Guía para el uso del sistema:\n\n"
    "n: número cuántico principal (nivel de energía). Valores permitidos: 1 a 5.\n"
    "l: número cuántico azimutal (subnivel). Valores: 0 ≤ l < n.\n"
    "m: número cuántico magnético. Valores: -l ≤ m ≤ l.\n\n"
    "Ejemplo válido:\nn = 3, l = 2, m = -2\n"
    "Ejemplo inválido:\nn = 2, l = 2 (porque l < n)"
    )
    mb.showinfo("Tutorial", mensaje)