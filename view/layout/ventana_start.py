from view.widgets.boton import boton_menu
# from view.widgets.number import number  # Ya no se usa esto
from view.widgets.combo import combobox
from view.widgets.counter import CounterWidget
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from .ventana import Ventana
import os
from controller import (mostrar_radial, mostrar_imag_esfericos, mostrar_real_esfericos,
                        mostrar_cartesian, mostrar_wf_2d, mostrar_wf_3d)


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
        label_numbers = QLabel("Escribe los números cuánticos:")
        label_numbers.setStyleSheet(parametros2)
        self.layout.addWidget(label_numbers, alignment=Qt.AlignHCenter)

        self.cnt_n = CounterWidget(title="Principal (n)", min_val=1, max_val=7, initial_val=3)
        self.cnt_l = CounterWidget(title="Azimuthal (l)", min_val=0, max_val=2, initial_val=0)
        self.cnt_m = CounterWidget(title="Magnetico (m)", min_val=0, max_val=0, initial_val=0)

        self.cnt_n.valueChanged.connect(self.update_l_limits)
        
        self.cnt_l.valueChanged.connect(self.update_m_limits)

        fila_nlm = QHBoxLayout()
        fila_nlm.addWidget(self.cnt_n)
        fila_nlm.addWidget(self.cnt_l)
        fila_nlm.addWidget(self.cnt_m)
        
        self.layout.addLayout(fila_nlm)

        callbacks = self.crear_callbacks(self.cnt_n, self.cnt_l, self.cnt_m)
        self.anadir_widgets(self.layout, callbacks)


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

        boton_radial = boton_menu("Función Radial", callbacks['on_radial'], 16, 150, 60, 10, 10)
        layout.addWidget(boton_radial, alignment=Qt.AlignTop)

        # Grupo 1: Spherical Harmonics
        grupo1 = QVBoxLayout()
        label1 = QLabel("Armónicos esféricos:")
        label1.setStyleSheet(parametros)
        combo1 = combobox(["Real", "Imaginarios"], on_change=on_combo1_changed)
        grupo1.addWidget(label1, alignment=Qt.AlignHCenter)
        grupo1.addWidget(combo1)

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
            from lib.class_electron import plot
            p = plot()

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

    def update_l_limits(self, new_n):
        """Actualiza el rango de l basado en el valor de n (0 a n-1)"""
        max_l = new_n - 1
        self.cnt_l.set_range(0, max_l)
        # Si l supera el nuevo máximo, se resetea automáticamente en set_range, 
        # pero forzamos un update de m por si acaso.
        self.update_m_limits(self.cnt_l.get_value())

    def update_m_limits(self, new_l):
        """Actualiza el rango de m basado en el valor de l (-l a +l)"""
        self.cnt_m.set_range(-new_l, new_l)

    def crear_callbacks(self, cnt_n, cnt_l, cnt_m):
        """Recibe los CounterWidget en lugar de los entry antiguos"""
        
        def on_radial():
            # Usar get_value() en lugar de .text()
            mostrar_radial(cnt_n.get_value(), cnt_l.get_value(), cnt_m.get_value())

        def on_real_esfericos():
            mostrar_real_esfericos(cnt_n.get_value(), cnt_l.get_value(), cnt_m.get_value())

        def on_imag():
            mostrar_imag_esfericos(cnt_n.get_value(), cnt_l.get_value(), cnt_m.get_value())

        def on_wf_2D():
            mostrar_wf_2d(cnt_n.get_value(), cnt_l.get_value(), cnt_m.get_value())

        def on_wf_3D():
            mostrar_wf_3d(cnt_n.get_value(), cnt_l.get_value(), cnt_m.get_value())

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
