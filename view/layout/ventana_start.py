from view.widgets.boton import boton_menu
from view.widgets.number import number
from view.widgets.combo import combobox
from PyQt5.QtWidgets import QMainWindow, QWidget, QSplitter, QLabel, QVBoxLayout, QApplication, QComboBox,QHBoxLayout
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtCore import Qt
from .ventana import Ventana
import os

class Start(Ventana):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.resize(600, 300)

    def init_ui(self):
        parametros = "color: white;font-family: 'Inter';font-weight: bold;font-size: 16px;"
        parametros2 = "color: white;font-family: 'Inter';font-weight: bold;font-size: 25px;"
        # 1. Define primero la función callback del botón.
        def mi_callback():
            print("¡Botón pequeño presionado!")

        def on_number_change(value):
            print(f"El usuario escribió: {value}")

        # 2. Sigue con el resto de la UI
        layout = QVBoxLayout()

        # Logo
        png_path = os.path.join("utils","quplotsLogo.png")
        label_logo = QLabel()
        pixmap = QPixmap(png_path)
        pixmap_reescalado = pixmap.scaled(200, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        # Asignar el QPixmap escalado al label
        label_logo.setPixmap(pixmap_reescalado)
        label_logo.setAlignment( Qt.AlignTop)
        label_logo.setFixedSize(200, 300)  #fijar el tamaño
        layout.addWidget(label_logo)

        label_numbers = QLabel("Enter the quantum numbers:")
        label_numbers.setStyleSheet(parametros2)
        layout.addWidget(label_numbers, alignment=Qt.AlignHCenter)

        
        # Layout horizontal para cada par
        campo_n = QHBoxLayout()
        label_n = QLabel("n:")
        label_n.setStyleSheet(parametros2)
        label_n.setFixedHeight(20)
        number_n = number(2, on_number_change)
        campo_n.addWidget(label_n)
        campo_n.addWidget(number_n)

        campo_l = QHBoxLayout()
        label_l = QLabel("l:")
        label_l.setStyleSheet(parametros2)
        label_l.setFixedHeight(20)
        number_l = number(2, on_number_change)
        campo_l.addWidget(label_l)
        campo_l.addWidget(number_l)

        campo_m = QHBoxLayout()
        label_m = QLabel("m:")
        label_m.setStyleSheet(parametros2)
        label_m.setFixedHeight(20)
        number_m = number(2, on_number_change)
        campo_m.addWidget(label_m)
        campo_m.addWidget(number_m)

        fila_nlm = QHBoxLayout()
        fila_nlm.addLayout(campo_n)
        fila_nlm.addSpacing(1) 
        fila_nlm.addLayout(campo_l)
        fila_nlm.addSpacing(1)
        fila_nlm.addLayout(campo_m)
        layout.addLayout(fila_nlm)

        label_plot = QLabel("Plot:")
        label_plot.setStyleSheet(parametros2)
        layout.addWidget(label_plot, alignment=Qt.AlignHCenter)

        #---- CADA LABEL+COMBO EN SU COLUMNA, LUEGO EN UNA FILA ----#
        btn_pequeno = boton_menu("Radial Function", mi_callback, 16, 150, 35,10,10)
        layout.addWidget(btn_pequeno, alignment=Qt.AlignTop)

        grupo1 = QVBoxLayout()
        label1 = QLabel("Spherical Harmonics:")
        label1.setStyleSheet(parametros)
        combo1 = combobox(
            ["Real", "Imaginary"],
            on_change=lambda idx: print(f"Combo 1 seleccionó {idx}")
        )
        grupo1.addWidget(label1, alignment=Qt.AlignHCenter)
        grupo1.addWidget(combo1, alignment=Qt.AlignHCenter)

        grupo2 = QVBoxLayout()
        label2 = QLabel("Probability Function:")
        label2.setStyleSheet(parametros)
        combo2 = combobox(
            ["2D", "3D"],
            on_change=lambda idx: print(f"Combo 2 seleccionó {idx}")
        )
        grupo2.addWidget(label2, alignment=Qt.AlignHCenter)
        grupo2.addWidget(combo2, alignment=Qt.AlignHCenter)

        grupo3 = QVBoxLayout()
        label3 = QLabel("Hybridization:")
        label3.setStyleSheet(parametros)
        combo3 = combobox(
            ["sp","sp²","sp³","sp²d","sp³d","sp³d²"],
            on_change=lambda idx: print(f"Combo 2 seleccionó {idx}")
        )
        grupo3.addWidget(label3, alignment=Qt.AlignHCenter)
        grupo3.addWidget(combo3, alignment=Qt.AlignHCenter)



        fila_combos = QHBoxLayout()
        fila_combos.addLayout(grupo1)
        fila_combos.addLayout(grupo2)
        fila_combos.addLayout(grupo3)
        fila= QHBoxLayout()
        fila.addWidget(btn_pequeno, alignment=Qt.AlignVCenter)
        fila.addSpacing(1)
        fila.addLayout(fila_combos)
        layout.addLayout(fila)

        
        label_costume = QLabel("Costume Style:")
        label_costume.setStyleSheet(parametros2)
        layout.addWidget(label_costume, alignment=Qt.AlignHCenter)

        # Splitter
        splitter = QSplitter(Qt.Horizontal)
        layout.addWidget(splitter)

        

        # Finaliza con el widget central
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def obtener_valores_desde_entry(entry_n=None,entry_l=None,entry_m=None):
        """
        Recibe los objetos entry_n,entry_l y entry_m. 
        se guardan los valores recibidos en formato de enteros. 
        Se devuelven los 3 numeros en formato de tupla
        """
        valores=[]
        for entry in (entry_n,entry_l,entry_m):
            if entry is not None:
                texto=entry.get().strip()
                if texto=="":
                    valores.append(None)
                else:
                    valores.append(int(texto))
        return tuple(valores)