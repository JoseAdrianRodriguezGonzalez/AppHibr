from view.widgets.boton import boton_menu
from view.widgets.combo import combobox
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt
from .ventana import Ventana
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

        self.current_color_scale = "Viridis"
        self.current_opacity = 0.5

        self.layout.setSpacing(15)
        self.layout.setContentsMargins(40, 30, 40, 30)

        self.init_ui()

    def init_ui(self):
        callbacks = self.crear_callbacks()
        self.anadir_widgets(self.layout, callbacks)

    def anadir_widgets(self, layout, callbacks):
        """Crea botones para cada seccion."""

        label_plot = QLabel("Graficar Hibridaciones Atomicas")
        label_plot.setStyleSheet("color: white;font-family: 'Inter';font-weight: bold;font-size: 20px;")
        label_plot.setAlignment(Qt.AlignHCenter)
        layout.addWidget(label_plot)

        label_estilo = QLabel("Editar colores de las graficas en 3D:")
        label_estilo.setStyleSheet("color: gray;font-family: 'Inter';font-weight: bold;font-size: 16px;")
        label_estilo.setAlignment(Qt.AlignHCenter)
        layout.addWidget(label_estilo)
        
        settings_row = QHBoxLayout()
        
        colorscales = ["Viridis", "Plasma", "Inferno", "Magma", "Cividis", "Rainbow", "Jet", "Portland", "Bluered", "RdBu"]
        
        def on_color_change(index):
            self.current_color_scale = colorscales[index]

        combo_colors = combobox(colorscales, on_change=on_color_change)
        
        opacities = [str(x) for x in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]]

        def on_opacity_change(index):
            self.current_opacity = float(opacities[index])

        combo_opacity = combobox(opacities, on_change=on_opacity_change)
        combo_opacity.setCurrentIndex(4)

        settings_row.addWidget(combo_colors)
        settings_row.addSpacing(20)
        settings_row.addWidget(combo_opacity)
        
        layout.addLayout(settings_row)

        p = plot()

        layout_hib_container = QVBoxLayout()
        layout_hib_container.setContentsMargins(0, 10, 0, 0) 
        layout_hib_container.setSpacing(10) 
        
        row1 = QHBoxLayout()
        btn_sp = boton_menu("sp", lambda: callbacks['on_hibridaciones'](p.plot_sp, self.current_color_scale, self.current_opacity), 14, 120, 40, 5, 5)
        row1.addWidget(btn_sp)

        btn_sp2 = boton_menu("sp²", lambda: callbacks['on_hibridaciones'](p.plot_sp2, self.current_color_scale, self.current_opacity), 14, 120, 40, 5, 5)
        row1.addWidget(btn_sp2)

        btn_sp3 = boton_menu("sp³", lambda: callbacks['on_hibridaciones'](p.plot_sp3, self.current_color_scale, self.current_opacity), 14, 120, 40, 5, 5)
        row1.addWidget(btn_sp3)

        row2 = QHBoxLayout()

        btn_sp2d = boton_menu("sp²d", lambda: callbacks['on_hibridaciones'](p.plot_sp2d, self.current_color_scale, self.current_opacity), 14, 120, 40, 5, 5)
        row2.addWidget(btn_sp2d)

        btn_sp3d = boton_menu("sp³d", lambda: callbacks['on_hibridaciones'](p.plot_sp3d, self.current_color_scale, self.current_opacity), 14, 120, 40, 5, 5)
        row2.addWidget(btn_sp3d)

        btn_sp3d2 = boton_menu("sp³d²", lambda: callbacks['on_hibridaciones'](p.plot_sp3d2, self.current_color_scale, self.current_opacity), 14, 120, 40, 5, 5)
        row2.addWidget(btn_sp3d2)

        layout_hib_container.addLayout(row1)
        layout_hib_container.addLayout(row2)
        
        layout.addLayout(layout_hib_container)
        layout.addStretch()

    def crear_callbacks(self):        
        def on_hibridaciones(plot_func, color_scale, opacity):
            mostrar_cartesian(plot_func, color_scale, opacity)

        return {
            'on_hibridaciones': on_hibridaciones
        }