from .ventana import Ventana
from view.widgets.boton import boton_menu
from view.widgets.counter import CounterWidget
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt
from .ventana import Ventana
import os
from controller import (mostrar_radial, mostrar_imag_esfericos, mostrar_real_esfericos, mostrar_wf_2d, mostrar_wf_3d)
from view.widgets.combo import combobox

class orbitales(Ventana):

    def __init__(self):
        super().__init__()

        # Crea el widget central
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)

        # Crea el layout principal
        self.layout = QVBoxLayout()
        self.main_widget.setLayout(self.layout)

        self.current_color_scale = "Viridis"
        
        # Inicializar UI
        self.init_ui()
    def init_ui(self):
        parametros2 = "color: white;font-family: 'Inter';font-weight: bold;font-size: 20px;"

        label_numbers = QLabel("Selecciona los números cuánticos:")
        label_numbers.setStyleSheet(parametros2)
        self.layout.addWidget(label_numbers, alignment=Qt.AlignLeft)

        self.cnt_n = CounterWidget(title="Principal (n)", min_val=1, max_val=20, initial_val=3)
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
        """Crea botones para cada sección y los organiza horizontalmente."""
        parametros = "color: gray;font-family: 'Inter';font-weight: bold;font-size: 16px;"

        # Label Principal
        label_plot = QLabel("Graficar :")
        label_plot.setStyleSheet("color: white;font-family: 'Inter';font-weight: bold;font-size: 20px;")
        layout.addWidget(label_plot, alignment=Qt.AlignLeft)
        
        label_radial = QLabel("Función Radial :")
        label_radial.setStyleSheet(parametros)
        layout.addWidget(label_radial, alignment=Qt.AlignHCenter)

        layout_radial = QHBoxLayout()
        boton_radial = boton_menu("2D", callbacks['on_radial'], 16, 150, 40, 5, 10)
        layout_radial.addWidget(boton_radial)
        layout.addLayout(layout_radial)

        label_esf = QLabel("Armónicos esféricos:")
        label_esf.setStyleSheet(parametros)
        layout.addWidget(label_esf, alignment=Qt.AlignHCenter)

        layout_esf = QHBoxLayout()
        boton_real = boton_menu("Real", callbacks['on_real_esfericos'], 16, 150, 40, 5, 5)
        boton_imag = boton_menu("Imaginarios", callbacks['on_imag'], 16, 150, 40, 5, 5)
        layout_esf.addWidget(boton_real)
        layout_esf.addWidget(boton_imag)
        layout.addLayout(layout_esf)

        label_prob = QLabel("Probability Function:")
        label_prob.setStyleSheet(parametros)
        layout.addWidget(label_prob, alignment=Qt.AlignHCenter)

        layout_prob = QHBoxLayout()
        boton_wf_2d = boton_menu("2D", callbacks['on_wf_2D'], 16, 150, 40, 5, 10)
        boton_wf_3d = boton_menu("3D", callbacks['on_wf_3D'], 16, 150, 40, 5, 10)
        layout_prob.addWidget(boton_wf_2d)
        layout_prob.addWidget(boton_wf_3d)
        layout.addLayout(layout_prob)

        layout.addStretch()

        
    def update_l_limits(self, new_n):
        """Actualiza el rango de l basado en el valor de n (0 a n-1)"""
        max_l = new_n - 1
        self.cnt_l.set_range(0, max_l)
        self.update_m_limits(self.cnt_l.get_value())

    def update_m_limits(self, new_l):
        """Actualiza el rango de m basado en el valor de l (-l a +l)"""
        self.cnt_m.set_range(-new_l, new_l)

    def crear_callbacks(self, cnt_n, cnt_l, cnt_m):
        """Recibe los CounterWidget en lugar de los entry antiguos"""
        
        def on_radial():
            mostrar_radial(cnt_n.get_value(), cnt_l.get_value(), cnt_m.get_value())

        def on_real_esfericos():
            mostrar_real_esfericos(cnt_n.get_value(), cnt_l.get_value(), cnt_m.get_value())

        def on_imag():
            mostrar_imag_esfericos(cnt_n.get_value(), cnt_l.get_value(), cnt_m.get_value())

        def on_wf_2D():
            mostrar_wf_2d(cnt_n.get_value(), cnt_l.get_value(), cnt_m.get_value())

        def on_wf_3D():
            mostrar_wf_3d(cnt_n.get_value(), cnt_l.get_value(), cnt_m.get_value())

        return {
            'on_radial': on_radial,
            'on_real_esfericos': on_real_esfericos,
            'on_imag': on_imag,
            'on_wf_2D': on_wf_2D,
            'on_wf_3D': on_wf_3D,
        }