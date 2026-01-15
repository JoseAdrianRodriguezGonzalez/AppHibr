import tkinter.messagebox as mb
def mostrar_error(titulo,mensaje):
    """
    Funcion contenedora del manejador de los mensajes de error tkinter.
    Si se desea cambiar eel framework, se debe modificar lo que se encuentra
    dentro de esta funcion
    Esta funcion recie dos strings, un titulo y el mensaje de error
    La funcion muestra una ventana con ambos strings
    """
    mb.showerror(titulo,mensaje)
def mostrar_tutorial():
    """
    Esta funcion genera una ventana que muestra la guia de uso del software
    """
    mensaje = (
    "Guía para el uso del sistema:\n\n"
    "n: número cuántico principal (nivel de energía). Valores permitidos: 1 a 5.\n"
    "l: número cuántico azimutal (subnivel). Valores: 0 ≤ l < n.\n"
    "m: número cuántico magnético. Valores: -l ≤ m ≤ l.\n\n"
    "Ejemplo válido:\nn = 3, l = 2, m = -2\n"
    "Ejemplo inválido:\nn = 2, l = 2 (porque l < n)"
    )
    mb.showinfo("Tutorial", mensaje)