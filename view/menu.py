import sys
from .layout import orbitales
from .layout import Start
from .widgets.boton import boton_menu
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QApplication, QWidget, QHBoxLayout
from .layout.ventana import Ventana
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtCore import Qt, QSize
import os

class MainMenu(Ventana):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        layout = QVBoxLayout()
        layout.addStretch()#espacio
        # logo 
        png_path = os.path.join("utils", "quplotsLogo.png")
        label_logo = QLabel()
        pixmap = QPixmap(png_path)
        label_logo.setPixmap(pixmap)
        label_logo.setAlignment(Qt.AlignCenter)
        label_logo.setFixedSize(600, 300)
        layout.addWidget(label_logo, alignment=Qt.AlignCenter)
        
        #botones
        btn_orbitales = boton_menu("Orbitales Atómicos", self.on_orbitales_clicked, 20,400,100)
        btn_start = boton_menu("Hibridaciones Atómicas", self.on_start_clicked, 20,400,100)

        h_layout = QHBoxLayout()
        h_layout.addWidget(btn_orbitales)
        h_layout.addWidget(btn_start)
        layout.addLayout(h_layout)
        layout.addStretch() #espacio

        #centrar los widgets
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


