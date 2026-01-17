import sys
from .layout import orbitales
from .layout import Start
from .widgets.boton import boton_menu
from .widgets.botonurl import boton_url
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QApplication, QWidget, QHBoxLayout
from .layout.ventana import Ventana
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtCore import Qt, QSize
import os

class MainMenu(Ventana):
    def __init__(self):
        super().__init__() # Asegúrate de llamar a super si tu clase hereda de Ventana/QMainWindow
        layout = QVBoxLayout()

        # 2. Espacio superior para centrar verticalmente
        layout.addStretch()

        # --- LOGO ---
        png_path = os.path.join("utils", "quplotsLogo.png")
        label_logo = QLabel()
        pixmap = QPixmap(png_path)
        # Escalamos el logo para que se vea bien sin deformarse
        pixmap = pixmap.scaled(300, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        label_logo.setPixmap(pixmap)
        label_logo.setAlignment(Qt.AlignCenter)
        layout.addWidget(label_logo, alignment=Qt.AlignCenter)

        # --- BOTONES PRINCIPALES ---
        btn_orbitales = boton_menu("Orbitales Atómicos", self.on_orbitales_clicked, 20, 400, 100)
        btn_start = boton_menu("Hibridaciones Atómicas", self.on_start_clicked, 20, 400, 100)

        # Layout horizontal para ponerlos uno al lado del otro
        h_layout_main = QHBoxLayout()
        h_layout_main.addWidget(btn_orbitales)
        h_layout_main.addWidget(btn_start)
        
        # --- TRUCO PARA CENTRAR LAYOUTS ---
        # Creamos un contenedor (Widget) para el layout
        container_main = QWidget()
        container_main.setLayout(h_layout_main)
        # Usamos addWidget (que sí permite alignment) para agregar el contenedor
        layout.addWidget(container_main, alignment=Qt.AlignHCenter)

        # --- BOTONES DE ENLACE (Web, Youtube) ---
        # Asegúrate de que boton_url esté definida o usa boton_menu si es lo mismo
        btn_web = boton_url("Página Web", url="https://joseadrianrodriguezgonzalez.github.io/Hybridization/")
        btn_yt = boton_url("Canal de Youtube", url="https://www.youtube.com/@quplots")

        # Layout horizontal para los enlaces
        h_layout_links = QHBoxLayout()
        h_layout_links.addWidget(btn_web)
        h_layout_links.addWidget(btn_yt)

        # --- TRUCO PARA CENTRAR LAYOUTS ---
        container_links = QWidget()
        container_links.setLayout(h_layout_links)
        layout.addWidget(container_links, alignment=Qt.AlignHCenter)

        # 3. Espacio inferior para centrar verticalmente
        layout.addStretch()

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def on_orbitales_clicked(self):
        self.ventana_orbitales = orbitales()
        self.ventana_orbitales.show()

    def on_start_clicked(self):
        self.ventana_start = Start()
        self.ventana_start.show()



def GUI():
    app = QApplication([])
    menu = MainMenu()
    menu.show()
    app.exec_()


