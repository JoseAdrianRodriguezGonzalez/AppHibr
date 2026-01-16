from view.widgets.boton import boton_menu
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt
from .ventana import Ventana
import os
from controller import mostrar_cartesian
from lib.class_electron import plot

class Start(Ventana):
    """
    Ventana dedicada exclusivamente a la Hibridación.
    """

    def __init__(self):
        super().__init__()

        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)

        self.layout = QVBoxLayout()
        self.main_widget.setLayout(self.layout)

        # --- AJUSTE DE ESPACIADO ---
        # Reduce el espacio entre los elementos principales (Título vs Botones)
        self.layout.setSpacing(10)
        # Define los bordes de la ventana (Izquierda, Arriba, Derecha, Abajo)
        self.layout.setContentsMargins(40, 30, 40, 30)

        # Inicializar UI
        self.init_ui()

    def init_ui(self):
        callbacks = self.crear_callbacks()
        self.anadir_widgets(self.layout, callbacks)

    def anadir_widgets(self, layout, callbacks):
        """Crea botones para cada seccion."""

        # Label Principal
        label_plot = QLabel("Graficar Hibridaciones Atomicas")
        label_plot.setStyleSheet("color: white;font-family: 'Inter';font-weight: bold;font-size: 20px;")
        label_plot.setAlignment(Qt.AlignHCenter)
        layout.addWidget(label_plot)

        label_estilo = QLabel("Editar colores de la grafica:")
        label_estilo.setStyleSheet("color: gray;font-family: 'Inter';font-weight: bold;font-size: 16px;")
        label_estilo.setAlignment(Qt.AlignHCenter)
        layout.addWidget(label_estilo)
        
        
        p = plot()

        layout_hib_container = QVBoxLayout()
        
        layout_hib_container.setContentsMargins(0, 10, 0, 0) 
        layout_hib_container.setSpacing(10) 
        
        row1 = QHBoxLayout()
        btn_sp = boton_menu("sp",lambda: callbacks['on_hibridaciones'](p.plot_sp), 14, 120, 40, 5, 5)
        row1.addWidget(btn_sp)

        btn_sp2 = boton_menu("sp²", lambda: callbacks['on_hibridaciones'](p.plot_sp2),14, 120, 40, 5, 5)
        row1.addWidget(btn_sp2)

        btn_sp3 = boton_menu("sp³",lambda: callbacks['on_hibridaciones'](p.plot_sp3),14, 120, 40, 5, 5)
        row1.addWidget(btn_sp3)

        row2 = QHBoxLayout()

        btn_sp2d = boton_menu("sp²d",lambda: callbacks['on_hibridaciones'](p.plot_sp2d),14, 120, 40, 5, 5)
        row2.addWidget(btn_sp2d)

        btn_sp3d = boton_menu("sp³d",lambda: callbacks['on_hibridaciones'](p.plot_sp3d),14, 120, 40, 5, 5)
        row2.addWidget(btn_sp3d)

        btn_sp3d2 = boton_menu("sp³d²", lambda: callbacks['on_hibridaciones'](p.plot_sp3d2), 14, 120, 40, 5, 5)
        row2.addWidget(btn_sp3d2)

        layout_hib_container.addLayout(row1)
        layout_hib_container.addLayout(row2)
        
        layout.addLayout(layout_hib_container)

        layout.addStretch()

    def crear_callbacks(self):        
        def on_hibridaciones(plot_func):
            mostrar_cartesian(plot_func)

        return {
            'on_hibridaciones': on_hibridaciones
        }