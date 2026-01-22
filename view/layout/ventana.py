from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QWidget
from PyQt5.QtCore import Qt

class Ventana(QMainWindow):
    """
    Clase base para todas las ventanas de la aplicación.
    Proporciona configuración común y estilo.
    """

    def __init__(self):
        super().__init__()
        self.setup_window()

    def setup_window(self):
        """Configuracion para todas las ventanas"""
        self.setWindowTitle("QuPlots")

        self.setStyleSheet("""
            QMainWindow {
                background-color: #010122;
            }
            QWidget {
                background-color: #010122;
                color: white;
            }
        """)

        self.setMinimumSize(600, 500)

        self.setWindowFlags(Qt.Window)

    def center_window(self):
        """Centra la ventana en la pantalla"""
        
        screen = QApplication.desktop().screenGeometry()
        size = self.geometry()
        self.move(
            int((screen.width() - size.width()) / 2),
            int((screen.height() - size.height()) / 2)
        )