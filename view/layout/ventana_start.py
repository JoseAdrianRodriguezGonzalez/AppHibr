from view.widgets.boton import boton_menu
from view.widgets.number import number
from view.widgets.combo import combobox
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from .ventana import Ventana
import os
from controller import (mostrar_radial,mostrar_imag_esfericos,mostrar_real_esfericos,
                                 mostrar_cartesian,mostrar_wf_2d,mostrar_wf_3d)


class Start(Ventana):
    """
    Ventana principal que usa las funciones del controller existente.
    Las gráficas se muestran en ventanas emergentes del navegador.
    """

    def __init__(self):
        super().__init__()

        # Crea el widget central
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)

        # Crea el layout principal
        self.layout = QVBoxLayout()
        self.main_widget.setLayout(self.layout)

        # Inicializar UI
        self.init_ui()
        self.resize(600, 700)

    def init_ui(self):
        parametros2 = "color: white;font-family: 'Inter';font-weight: bold;font-size: 25px;"

        # Logo
        png_path = os.path.join("utils", "quplotsLogo.png")
        label_logo = QLabel()
        pixmap = QPixmap(png_path)
        if not pixmap.isNull():
            pixmap_reescalado = pixmap.scaled(200, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            label_logo.setPixmap(pixmap_reescalado)
        label_logo.setAlignment(Qt.AlignTop)
        label_logo.setFixedSize(200, 300)
        self.layout.addWidget(label_logo)

        # Label de instrucciones
        label_numbers = QLabel("Enter quantum numbers:")
        label_numbers.setStyleSheet(parametros2)
        self.layout.addWidget(label_numbers, alignment=Qt.AlignHCenter)

        # Layout horizontal para n, l, m
        campo_n = QHBoxLayout()
        label_n = QLabel("n:")
        label_n.setStyleSheet(parametros2)
        label_n.setFixedHeight(20)
        entry_n = number(2)
        campo_n.addWidget(label_n)
        campo_n.addWidget(entry_n)

        campo_l = QHBoxLayout()
        label_l = QLabel("l:")
        label_l.setStyleSheet(parametros2)
        label_l.setFixedHeight(20)
        entry_l = number(0)
        campo_l.addWidget(label_l)
        campo_l.addWidget(entry_l)

        campo_m = QHBoxLayout()
        label_m = QLabel("m:")
        label_m.setStyleSheet(parametros2)
        label_m.setFixedHeight(20)
        entry_m = number(0)
        campo_m.addWidget(label_m)
        campo_m.addWidget(entry_m)

        fila_nlm = QHBoxLayout()
        fila_nlm.addLayout(campo_n)
        fila_nlm.addSpacing(1)
        fila_nlm.addLayout(campo_l)
        fila_nlm.addSpacing(1)
        fila_nlm.addLayout(campo_m)
        self.layout.addLayout(fila_nlm)

        # Crear callbacks y widgets
        callbacks = self.crear_callbacks(entry_n, entry_l, entry_m)
        self.anadir_widgets(self.layout, callbacks)

        # Label informativo
        label_info = QLabel("Las graficas se abriran en el navegador")
        label_info.setStyleSheet("color: #888888; font-size: 12px;")
        self.layout.addWidget(label_info, alignment=Qt.AlignCenter)

    def anadir_widgets(self, layout, callbacks):
        """Crea los botones y combobox para graficar."""
        parametros = "color: white;font-family: 'Inter';font-weight: bold;font-size: 16px;"
        parametros2 = "color: white;font-family: 'Inter';font-weight: bold;font-size: 25px;"

        # Label Plot
        label_plot = QLabel("Plot:")
        label_plot.setStyleSheet(parametros2)
        layout.addWidget(label_plot, alignment=Qt.AlignHCenter)

        # Combo 1: Spherical Harmonics
        def on_combo1_changed(index):
            if index == 0:
                callbacks['on_real_esfericos']()
            elif index == 1:
                callbacks['on_imag']()

        # Botón Radial
        boton_radial = boton_menu("Radial Function", callbacks['on_radial'], 16, 150, 35, 10, 10)
        layout.addWidget(boton_radial, alignment=Qt.AlignTop)

        # Grupo 1: Spherical Harmonics
        grupo1 = QVBoxLayout()
        label1 = QLabel("Spherical Harmonics:")
        label1.setStyleSheet(parametros)
        combo1 = combobox(["Real", "Imaginary"], on_change=on_combo1_changed)
        grupo1.addWidget(label1, alignment=Qt.AlignHCenter)
        grupo1.addWidget(combo1)

        # Combo 2: Probability Function
        def on_combo2_changed(index):
            print(f"\n--- Evento combo2 cambiado a indice {index} ---")
            try:
                if index == 0:
                    print("DEBUG: Opcion 2D seleccionada")
                    if 'on_wf_2D' not in callbacks:
                        print("ERROR: No existe callback 'on_wf_2D'")
                        return
                    print("DEBUG: Ejecutando callback on_wf_2D")
                    callbacks['on_wf_2D']()
                elif index == 1:
                    print("DEBUG: Opcion 3D seleccionada")
                    callbacks['on_wf_3D']()
            except Exception as e:
                print(f"ERROR CRITICO en on_combo2_changed: {str(e)}")

        grupo2 = QVBoxLayout()
        label2 = QLabel("Probability Function:")
        label2.setStyleSheet(parametros)
        combo2 = combobox(["2D", "3D"], on_change=on_combo2_changed)
        grupo2.addWidget(label2, alignment=Qt.AlignHCenter)
        grupo2.addWidget(combo2)

        # Combo 3: Hybridization
        def on_combo3_changed(index):
            # Importar la clase plot desde class_electron
            from lib.class_electron import plot
            p = plot()

            # Definir las funciones de hibridacion de la clase plot
            opciones = [
                p.plot_sp,
                p.plot_sp2,
                p.plot_sp3,
                p.plot_sp2d,
                p.plot_sp3d,
                p.plot_sp3d2
            ]
            if 0 <= index < len(opciones):
                callbacks['on_hibridaciones'](opciones[index])

        grupo3 = QVBoxLayout()
        label3 = QLabel("Hybridization:")
        label3.setStyleSheet(parametros)
        combo3 = combobox(
            ["sp", "sp²", "sp³", "sp²d", "sp³d", "sp³d²"],
            on_change=on_combo3_changed
        )
        grupo3.addWidget(label3, alignment=Qt.AlignHCenter)
        grupo3.addWidget(combo3)

        # Layout de combos
        fila_combos = QHBoxLayout()
        fila_combos.addLayout(grupo1)
        fila_combos.addLayout(grupo2)
        fila_combos.addLayout(grupo3)

        fila = QHBoxLayout()
        fila.addWidget(boton_radial, alignment=Qt.AlignVCenter)
        fila.addSpacing(1)
        fila.addLayout(fila_combos)
        layout.addLayout(fila)

    def crear_callbacks(self, entry_n, entry_l, entry_m):
        """Crea las funciones callback usando las funciones del controller."""
        
        def on_radial():
            print("Callback: on_radial")
            values = self.obtener_valores_desde_entry(entry_n, entry_l, entry_m)
            print(f"Valores ingresados: n={values[0]}, l={values[1]}, m={values[2]}")
            mostrar_radial(values[0], values[1], values[2])

        def on_real_esfericos():
            values = self.obtener_valores_desde_entry(entry_n, entry_l, entry_m)
            mostrar_real_esfericos(values[0], values[1], values[2])

        def on_imag():
            values = self.obtener_valores_desde_entry(entry_n, entry_l, entry_m)
            mostrar_imag_esfericos(values[0], values[1], values[2])

        def on_wf_2D():
            print("\n--- Ejecutando on_wf_2D ---")
            try:
                values = self.obtener_valores_desde_entry(entry_n, entry_l, entry_m)
                print(f"DEBUG: Valores obtenidos - n:{values[0]}, l:{values[1]}, m:{values[2]}")
                mostrar_wf_2d(values[0], values[1], values[2])
            except Exception as e:
                print(f"ERROR en on_wf_2D: {str(e)}")

        def on_wf_3D():
            values = self.obtener_valores_desde_entry(entry_n, entry_l, entry_m)
            mostrar_wf_3d(values[0], values[1], values[2])

        def on_hibridaciones(plot_func):
            mostrar_cartesian(plot_func)

        return {
            'on_radial': on_radial,
            'on_real_esfericos': on_real_esfericos,
            'on_imag': on_imag,
            'on_wf_2D': on_wf_2D,
            'on_wf_3D': on_wf_3D,
            'on_hibridaciones': on_hibridaciones
        }

    def obtener_valores_desde_entry(self, entry_n=None, entry_l=None, entry_m=None):
        """
        Obtiene valores de los campos de entrada.
        Devuelve los valores en formato de tupla.
        """
        valores = []
        for i, entry in enumerate((entry_n, entry_l, entry_m), start=1):
            if entry is not None:
                try:
                    texto = entry.text().strip()
                    if texto == "":
                        valores.append(None)
                    else:
                        valores.append(int(texto))
                except Exception as ex:
                    print(f"Error al procesar el campo {i}:", ex)
                    valores.append(None)
            else:
                valores.append(None)

        return tuple(valores)