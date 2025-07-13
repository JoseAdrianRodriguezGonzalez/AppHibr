import time 
import tkinter as tk
import os
from tkinter import messagebox
import numpy as np
import pickle
from class_electron import electron, plot
e = electron()
p = plot()
def guardar_datos(nombre_archivo, datos):
    os.makedirs(os.path.dirname(nombre_archivo),exist_ok=True)
    with open(nombre_archivo, "wb") as f:
        pickle.dump(datos, f)
def cargar_datos(nombre_archivo):
    try:
        with open(nombre_archivo, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return None
def validar_entradas():
    n = int(entry_n.get())
    l = int(entry_l.get())
    m = int(entry_m.get())
    if n <= 0 or l < 0 or l >= n or not (-l <= m <= l):
        raise ValueError("Debe cumplirse: n > 0, 0 ≤ l < n, y -l ≤ m ≤ l.")
    return n, l, m
def calcular_radial():
    try:
        n, l, _ = validar_entradas()
        radial_file = f"data/radial_{n}_{l}.pkl"
        start=time.time()
        radial_data = cargar_datos(radial_file)
        if radial_data is None:
            radial_data = e.RealSpherical(n, l)
            guardar_datos(radial_file, radial_data)
            print(f"Tiempo de calculo  radiial:{time.time()-start:.4f} s")
        else:
            print(f"Tiempo de **carga** radial: {time.time() - start:.4f} s")
        p.plot_radial_(2, n, l)
    except Exception as ex:
        messagebox.showerror("Error", str(ex))  
def calcular_wf_2d():
    try:
        n, l, m = validar_entradas()
        wf_2d_file = f"data/wf_2d_{n}_{l}_{m}.npy"
        start=time.time()
        wf_2d = cargar_datos(wf_2d_file)
        if wf_2d is None:
            wf_2d = e.normalized_wf(500, n, l, m)
            guardar_datos(wf_2d_file, wf_2d)
            print(f"Tiempo de calculo  wf_2d:{time.time()-start:.4f} s")
        else:
            print(f"Tiempo de **carga** de wf_2d: {time.time() - start:.4f} s")
        p.plot_wf_2d(wf_2d)
    except Exception as ex:
        messagebox.showerror("Error", str(ex))
def calcular_wf_3d():
    try:
        n, l, m = validar_entradas()
        wf_3d_file = f"data/wf_3d_{n}_{l}_{m}.npy"
        start=time.time()
        wf_3d = cargar_datos(wf_3d_file)
        if wf_3d is None:
            wf_3d = e.normalized_wf3D(n, l, m)
            guardar_datos(wf_3d_file, wf_3d)
            print(f"Tiempo de calculo  wf_3d:{time.time()-start:.4f} s")
        else:
            print(f"Tiempo de **carga** de wf_3d: {time.time() - start:.4f} s")
        bg_color = bg_color_var.get()
        font_color = font_color_var.get()
        colorscale = colorscale_var.get()
        p.plot_wf_3d(wf_3d)
        #p.plot_wf_3d(wf_3d, colorscale=colorscale, background=bg_color, font_color=font_color)
    except Exception as ex:
        messagebox.showerror("Error", str(ex))
def mostrar_spherical_real():
    try:
        _, l, m = validar_entradas()
        archivo = f"data/spherical_real_{l}_{m}.pkl"
        start=time.time()
        datos = cargar_datos(archivo)
        if datos is None:
            datos = e.RealSpherical(l, m)
            guardar_datos(archivo, datos)
            print(f"Tiempo de calculo  spherical real:{time.time()-start:.4f} s")
        else:
            print(f"Tiempo de **carga** de spherical real: {time.time() - start:.4f} s")
        p.plot_spherical_real(datos)
    except Exception as ex:
        messagebox.showerror("Error", str(ex))
def mostrar_spherical_imag():
    try:
        _, l, m = validar_entradas()
        archivo = f"data/spherical_imaginary_{l}_{m}.pkl"
        start=time.time()
        datos = cargar_datos(archivo)
        if datos is None:
            datos = e.ImaginarySpherical(l, m)
            guardar_datos(archivo, datos)
            print(f"Tiempo de calculo spherical_img:{time.time()-start:.4f} s")
        else:
            print(f"Tiempo de **carga** de spherical_img: {time.time() - start:.4f} s")
        p.plot_spherical_imaginary(datos)
    except Exception as ex:
        messagebox.showerror("Error", str(ex))
def mostrar_cartesian(func):
    try:
        archivo = "data/cartesian.pkl"
        start=time.time()
        datos = cargar_datos(archivo)
        if datos is None:
            datos = e.Cartesian_definition()
            guardar_datos(archivo, datos)
            print(f"Tiempo de calculo  cartesian:{time.time()-start:.4f} s")
        else:
            print(f"Tiempo de **carga** de cartesian: {time.time() - start:.4f} s")
        func(datos)
    except Exception as ex:
        messagebox.showerror("Error", str(ex))
    except Exception as ex:
        messagebox.showerror("Error", str(ex))
def mostrar_tutorial():
    mensaje = (
    "Guía para el uso del sistema:\n\n"
    "n: número cuántico principal (nivel de energía). Valores permitidos: 1 a 5.\n"
    "l: número cuántico azimutal (subnivel). Valores: 0 ≤ l < n.\n"
    "m: número cuántico magnético. Valores: -l ≤ m ≤ l.\n\n"
    "Ejemplo válido:\nn = 3, l = 2, m = -2\n"
    "Ejemplo inválido:\nn = 2, l = 2 (porque l < n)"
    )
    messagebox.showinfo("Tutorial", mensaje)
# Crear GUI
root = tk.Tk()
root.title("Calculadora de Orbitales")
root.geometry("500x430")
root.configure(bg="white")
entry_n = tk.Entry(root, width=10)
entry_l = tk.Entry(root, width=10)
entry_m = tk.Entry(root, width=10)
entry_n.grid(row=0, column=0, padx=10, pady=10)
entry_l.grid(row=0, column=1, padx=10, pady=10)
entry_m.grid(row=0, column=2, padx=10, pady=10)
tk.Label(root, text="n", bg="white").grid(row=1, column=0)
tk.Label(root, text="l", bg="white").grid(row=1, column=1)
tk.Label(root, text="m", bg="white").grid(row=1, column=2)
# Menús de selección de color

colores_disponibles = ["black", "white", "lightgray", "darkblue", "navy", "red", "green", "purple", "orange"]
colormaps_disponibles = ["Viridis", "Plasma", "Inferno", "Magma", "Cividis", "Rainbow", "Jet", "Portland", "Bluered", "RdBu"]
bg_color_var = tk.StringVar(value="black")
font_color_var = tk.StringVar(value="white")
colorscale_var = tk.StringVar(value="RdBu")
tk.Label(root, text="Color Fondo 3D", bg="white").grid(row=5, column=0)

tk.OptionMenu(root, bg_color_var, *colores_disponibles).grid(row=5, column=1)
tk.Label(root, text="Color Texto 3D", bg="white").grid(row=6, column=0)
tk.OptionMenu(root, font_color_var, *colores_disponibles).grid(row=6, column=1)
tk.Label(root, text="Colormap Figura 3D", bg="white").grid(row=7, column=0)
tk.OptionMenu(root, colorscale_var, *colormaps_disponibles).grid(row=7, column=1)

# Botones principales
tk.Button(root, text="Calcular Radial", command=calcular_radial, bg="#4682B4", fg="white").grid(row=2, column=0, pady=10)
tk.Button(root, text="Función 2D", command=calcular_wf_2d, bg="#32CD32", fg="white").grid(row=2, column=1, pady=10)
tk.Button(root, text="Función 3D", command=calcular_wf_3d, bg="#FFA500", fg="white").grid(row=2, column=2, pady=10)
tk.Button(root, text="Sph. Real", command=mostrar_spherical_real, bg="#4B0082", fg="white").grid(row=8, column=0, pady=5)
tk.Button(root, text="Sph. Imag.", command=mostrar_spherical_imag, bg="#483D8B", fg="white").grid(row=8, column=1, pady=5)
tk.Button(root, text="sp", command=lambda: mostrar_cartesian(p.plot_sp), bg="#708090", fg="white").grid(row=9, column=0, pady=5)
tk.Button(root, text="sp2", command=lambda: mostrar_cartesian(p.plot_sp2), bg="#708090", fg="white").grid(row=9, column=1, pady=5)
tk.Button(root, text="sp3", command=lambda: mostrar_cartesian(p.plot_sp3), bg="#708090", fg="white").grid(row=9, column=2, pady=5)
tk.Button(root, text="sp2d", command=lambda: mostrar_cartesian(p.plot_sp2d), bg="#2F4F4F", fg="white").grid(row=10, column=0, pady=5)
tk.Button(root, text="sp3d", command=lambda: mostrar_cartesian(p.plot_sp3d), bg="#2F4F4F", fg="white").grid(row=10, column=1, pady=5)
tk.Button(root, text="sp3d2", command=lambda: mostrar_cartesian(p.plot_sp3d2), bg="#2F4F4F", fg="white").grid(row=10, column=2, pady=5)
tk.Button(root, text="Tutorial", command=mostrar_tutorial, bg="#555555", fg="white").grid(row=4, column=1, pady=10)
root.mainloop()