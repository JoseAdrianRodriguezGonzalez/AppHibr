import tkinter as tk
from lib.class_electron import plot
from utils import mostrar_tutorial
from controller import (mostrar_radial,mostrar_imag_esfericos,mostrar_real_esfericos,
                                mostrar_cartesian,mostrar_wf_2d,mostrar_wf_3d)
def obtener_valores_desde_entry(entry_n=None,entry_l=None,entry_m=None):
    valores=[]
    for entry in (entry_n,entry_l,entry_m):
        if entry is not None:
            texto=entry.get().strip()
            if texto=="":
                valores.append(None)
            else:
                valores.append(int(texto))
    return tuple(valores)
def init_root():
    root = tk.Tk()
    root.title("Calculadora de Orbitales")
    root.geometry("500x430")
    root.configure(bg="white")
    return root
def init_entries(root):
    entry_n = tk.Entry(root, width=10)
    entry_l = tk.Entry(root, width=10)
    entry_m = tk.Entry(root, width=10)
    entry_n.grid(row=0, column=0, padx=10, pady=10)
    entry_l.grid(row=0, column=1, padx=10, pady=10)
    entry_m.grid(row=0, column=2, padx=10, pady=10)
    return entry_n,entry_l,entry_m
def crear_menu_colores(root):
    
    tk.Label(root, text="n", bg="white").grid(row=1, column=0)
    tk.Label(root, text="l", bg="white").grid(row=1, column=1)
    tk.Label(root, text="m", bg="white").grid(row=1, column=2)
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
    return bg_color_var,font_color_var,colorscale_var
def widgets(root,callbacks):
    p=plot()
    tk.Button(root, text="Calcular Radial", command=callbacks['on_radial'], bg="#4682B4", fg="white").grid(row=2, column=0, pady=10)
    tk.Button(root, text="Función 2D", command=callbacks['on_wf_2D'], bg="#32CD32", fg="white").grid(row=2, column=1, pady=10)
    tk.Button(root, text="Función 3D", command=callbacks['on_wf_3D'], bg="#FFA500", fg="white").grid(row=2, column=2, pady=10)
    tk.Button(root, text="Sph. Real", command=callbacks['on_real_esfericos'], bg="#4B0082", fg="white").grid(row=8, column=0, pady=5)
    tk.Button(root, text="Sph. Imag.", command=callbacks['on_imag'], bg="#483D8B", fg="white").grid(row=8, column=1, pady=5)
    tk.Button(root, text="sp", command=lambda: callbacks['on_hibridaciones'](p.plot_sp), bg="#708090", fg="white").grid(row=9, column=0, pady=5)
    tk.Button(root, text="sp2", command=lambda:callbacks['on_hibridaciones'](p.plot_sp2), bg="#708090", fg="white").grid(row=9, column=1, pady=5)
    tk.Button(root, text="sp3", command=lambda: callbacks['on_hibridaciones'](p.plot_sp3), bg="#708090", fg="white").grid(row=9, column=2, pady=5)
    tk.Button(root, text="sp2d", command=lambda: callbacks['on_hibridaciones'](p.plot_sp2d), bg="#2F4F4F", fg="white").grid(row=10, column=0, pady=5)
    tk.Button(root, text="sp3d", command=lambda: callbacks['on_hibridaciones'](p.plot_sp3d), bg="#2F4F4F", fg="white").grid(row=10, column=1, pady=5)
    tk.Button(root, text="sp3d2", command=lambda: callbacks['on_hibridaciones'](p.plot_sp3d2), bg="#2F4F4F", fg="white").grid(row=10, column=2, pady=5)
    tk.Button(root, text="Tutorial", command=mostrar_tutorial, bg="#555555", fg="white").grid(row=4, column=1, pady=10)
def crear_callbacks(entry_n,entry_l,entry_m):
    def on_radial():
        values=obtener_valores_desde_entry(entry_n,entry_l,entry_m)
        mostrar_radial(values[0],values[1],values[2])
    def on_real_esfericos():
        values=obtener_valores_desde_entry(entry_n,entry_l,entry_m)
        mostrar_real_esfericos(values[0],values[1],values[2])
    def on_imag():
        values=obtener_valores_desde_entry(entry_n,entry_l,entry_m)
        mostrar_imag_esfericos(values[0],values[1],values[2])
    def on_wf_2D():
        values=obtener_valores_desde_entry(entry_n,entry_l,entry_m)
        mostrar_wf_2d(values[0],values[1],values[2])
    def on_wf_3D():
        values=obtener_valores_desde_entry(entry_n,entry_l,entry_m)
        mostrar_wf_3d(values[0],values[1],values[2])
    def on_hibridaciones(func):
        mostrar_cartesian(func)
    return {
        'on_radial': on_radial,
        'on_real_esfericos': on_real_esfericos,
        'on_imag': on_imag,
        'on_wf_2D': on_wf_2D,
        'on_wf_3D': on_wf_3D,
        'on_hibridaciones': on_hibridaciones
    }
def GUI():
    root = init_root()
    entry_n, entry_l, entry_m = init_entries(root)
    bg_var, font_var, colormap_var = crear_menu_colores(root)
    callbacks = crear_callbacks(entry_n, entry_l, entry_m)
    widgets(root,callbacks)
    root.mainloop()
