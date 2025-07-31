import sys
from .layout import Theory
from .layout import Start
from .layout import Tutorial
# from layout.ventana_start import Start
# from layout.ventana_tutorial import Tutorial
from .widgets.boton import boton_menu
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QApplication, QWidget, QHBoxLayout
from .layout.ventana import Ventana
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtSvg import QSvgRenderer
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
        label_logo.setFixedSize(600, 300)  # Opcional: fija el tamaño del QLabel
        layout.addWidget(label_logo, alignment=Qt.AlignCenter)
        
        #botones
        btn_theory = boton_menu("Theory", self.on_theory_clicked)
        btn_start = boton_menu("Start", self.on_start_clicked)
        btn_tutorial = boton_menu("Tutorial", self.on_tutorial_clicked)

        h_layout = QHBoxLayout()
        h_layout.addWidget(btn_theory)
        h_layout.addWidget(btn_start)
        h_layout.addWidget(btn_tutorial)
        layout.addLayout(h_layout)
        layout.addStretch() #espacio

        #centrar los widgets
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def on_theory_clicked(self):
        self.ventana_theory = Theory()
        self.ventana_theory.show()

    def on_start_clicked(self):
        self.ventana_start = Start()
        self.ventana_start.show()

    def on_tutorial_clicked(self):
        self.ventana_tutorial = Tutorial()
        self.ventana_tutorial.show()

def GUI():
    app = QApplication([])
    menu = MainMenu()
    menu.show()
    app.exec_()