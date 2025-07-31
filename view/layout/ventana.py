from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon, QPalette, QColor
import sys

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.caracteristicas()

    def caracteristicas(self):
        self.setWindowTitle("QuPlots")
        self.setWindowIcon(QIcon("utils\\sp.png"))
        self.setFixedSize(1000,600)
        palette =self.palette()
        palette.setColor(QPalette.Window, QColor("#020216"))
        self.setPalette(palette)
