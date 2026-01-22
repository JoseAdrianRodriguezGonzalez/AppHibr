import sys
from .layout import orbitales
from .layout import Start
from .widgets.boton import boton_menu
from .widgets.botonurl import boton_url
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QApplication, QWidget, QHBoxLayout
from .layout.ventana import Ventana
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import os

class MainMenu(Ventana):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        layout.addStretch()

        png_path = os.path.join("utils", "quplotsLogo.png")
        label_logo = QLabel()
        pixmap = QPixmap(png_path)
        pixmap = pixmap.scaled(300, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        label_logo.setPixmap(pixmap)
        label_logo.setAlignment(Qt.AlignCenter)
        layout.addWidget(label_logo, alignment=Qt.AlignCenter)

        btn_orbitales = boton_menu("Orbitales Atómicos", self.on_orbitales_clicked, 20, 400, 100)
        btn_start = boton_menu("Hibridaciones Atómicas", self.on_start_clicked, 20, 400, 100)

        h_layout_main = QHBoxLayout()
        h_layout_main.addWidget(btn_orbitales)
        h_layout_main.addWidget(btn_start)
        
        container_main = QWidget()
        container_main.setLayout(h_layout_main)
        layout.addWidget(container_main, alignment=Qt.AlignHCenter)

        btn_web = boton_url("Documentación", url="https://joseadrianrodriguezgonzalez.github.io/Hybridization/" )
        btn_yt = boton_url("Videos", url="https://www.youtube.com/@quplots")

        h_layout_links = QHBoxLayout()
        h_layout_links.addWidget(btn_web)
        h_layout_links.addWidget(btn_yt)

        container_links = QWidget()
        container_links.setLayout(h_layout_links)
        layout.addWidget(container_links, alignment=Qt.AlignRight)

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


