from view.widgets.boton import boton_menu
from view.widgets.number import number
from view.widgets.combo import combobox
from PyQt5.QtWidgets import QMainWindow, QWidget, QSplitter, QLabel, QVBoxLayout, QApplication, QComboBox,QHBoxLayout
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtCore import Qt
from .ventana import Ventana
import os
from lib.class_electron import plot
from controller import (mostrar_radial,mostrar_imag_esfericos,mostrar_real_esfericos,
                                mostrar_cartesian,mostrar_wf_2d,mostrar_wf_3d)

class Start(Ventana):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.resize(600, 300)

    def init_ui(self):
        parametros = "color: white;font-family: 'Inter';font-weight: bold;font-size: 16px;"
        parametros2 = "color: white;font-family: 'Inter';font-weight: bold;font-size: 25px;"

        layout = QVBoxLayout()



        def on_number_change(value):
            print(f"numero: {value}")


        #logo
        png_path = os.path.join("utils","quplotsLogo.png")
        label_logo = QLabel()
        pixmap = QPixmap(png_path)
        pixmap_reescalado = pixmap.scaled(200, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        #escalado al label
        label_logo.setPixmap(pixmap_reescalado)
        label_logo.setAlignment( Qt.AlignTop)
        label_logo.setFixedSize(200, 300)  #fijar el tamaño
        layout.addWidget(label_logo)

        label_numbers = QLabel("Enter the quantum numbers:")
        label_numbers.setStyleSheet(parametros2)
        layout.addWidget(label_numbers, alignment=Qt.AlignHCenter)

        
        #layout horizontal
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
        callbacks = self.crear_callbacks(number_n, number_l, number_m)
        self.anadir_widgets(layout, callbacks)

        

    def anadir_widgets(self, layout,callbacks):
        """
        Se crean los botones que permiten graficar.
        Se pasa el objeto de root y los callbacks, que es un diccionario con strings y funciones
        """
        #labels con columna

        parametros = "color: white;font-family: 'Inter';font-weight: bold;font-size: 16px;"
        parametros2 = "color: white;font-family: 'Inter';font-weight: bold;font-size: 25px;"
        #plot
        label_plot = QLabel("Plot:")
        label_plot.setStyleSheet(parametros2)
        layout.addWidget(label_plot, alignment=Qt.AlignHCenter)

        def on_combo1_changed(index):
            if index == 0:
                callbacks['on_real_esfericos']()
            elif index == 1:
                callbacks['on_imag']()

        boton_radial = boton_menu("Radial Function", callbacks['on_radial'], 16, 150, 35,10,10)
        layout.addWidget(boton_radial, alignment=Qt.AlignTop)

        grupo1 = QVBoxLayout()
        label1 = QLabel("Spherical Harmonics:")
        label1.setStyleSheet(parametros)
        combo1 = combobox(
            ["Real", "Imaginary"],on_change=on_combo1_changed)
        grupo1.addWidget(label1, alignment=Qt.AlignHCenter)
        grupo1.addWidget(combo1, alignment=Qt.AlignHCenter)

        def on_combo2_changed(index):
            if index == 0:
                callbacks['on_wf_2D']()
            elif index == 1:
                callbacks['on_wf_3D']()

        grupo2 = QVBoxLayout()
        label2 = QLabel("Probability Function:")
        label2.setStyleSheet(parametros)
        combo2 = combobox(
            ["2D", "3D"],on_change=on_combo2_changed)
        grupo2.addWidget(label2, alignment=Qt.AlignHCenter)
        grupo2.addWidget(combo2, alignment=Qt.AlignHCenter)


        def on_combo3_changed(index):
            p=plot()
            if index == 0:
                callbacks['on_hibridaciones'](p.plot_sp)
            elif index == 1:  
                callbacks['on_hibridaciones'](p.plot_sp2)
            elif index == 2:  
                callbacks['on_hibridaciones'](p.plot_sp3)
            elif index == 3:  
                callbacks['on_hibridaciones'](p.plot_sp2d)
            elif index == 4:  
                callbacks['on_hibridaciones'](p.plot_sp3d)
            elif index == 5:  
                callbacks['on_hibridaciones'](p.plot_sp3d2)

        grupo3 = QVBoxLayout()
        label3 = QLabel("Hybridization:")
        label3.setStyleSheet(parametros)
        combo3 = combobox(
            ["sp","sp²","sp³","sp²d","sp³d","sp³d²"],on_change=on_combo3_changed)
        grupo3.addWidget(label3, alignment=Qt.AlignHCenter)
        grupo3.addWidget(combo3, alignment=Qt.AlignHCenter)


        fila_combos = QHBoxLayout()
        fila_combos.addLayout(grupo1)
        fila_combos.addLayout(grupo2)
        fila_combos.addLayout(grupo3)
        fila= QHBoxLayout()
        fila.addWidget(boton_radial, alignment=Qt.AlignVCenter)
        fila.addSpacing(1)
        fila.addLayout(fila_combos)
        layout.addLayout(fila)

        
        label_costume = QLabel("Costume Style:")
        label_costume.setStyleSheet(parametros2)
        layout.addWidget(label_costume, alignment=Qt.AlignHCenter)

        # Splitter
        splitter = QSplitter(Qt.Horizontal)
        layout.addWidget(splitter)

        
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def crear_callbacks(self,entry_n,entry_l,entry_m):
        """
        Se definen las funciones de callback que seran retornados en forma de diccionario
        En la entrada se ingresa los datos de entry_n,entry_l,entry_m.
        En cada funcion de callback que toma los entry,se validan los elementos 
        """
        def on_radial():
            values=self.obtener_valores_desde_entry(entry_n,entry_l,entry_m)
            mostrar_radial(values[0],values[1],values[2])
        def on_real_esfericos():
            values=self.obtener_valores_desde_entry(entry_n,entry_l,entry_m)
            mostrar_real_esfericos(values[0],values[1],values[2])
        def on_imag():
            values=self.obtener_valores_desde_entry(entry_n,entry_l,entry_m)
            mostrar_imag_esfericos(values[0],values[1],values[2])
        def on_wf_2D():
            values=self.obtener_valores_desde_entry(entry_n,entry_l,entry_m)
            mostrar_wf_2d(values[0],values[1],values[2])
        def on_wf_3D():
            values=self.obtener_valores_desde_entry(entry_n,entry_l,entry_m)
            mostrar_wf_3d(values[0],values[1],values[2])
        def on_hibridaciones(func):
            mostrar_cartesian(func)

        return {
            'on_radial': on_radial,
            'on_real_esfericos': on_real_esfericos,
            'on_imag': on_imag,
            'on_wf_2D': on_wf_2D,
            'on_wf_3D': on_wf_3D,
            'on_hibridaciones': on_hibridaciones
        }

    def obtener_valores_desde_entry(self,entry_n=None,entry_l=None,entry_m=None):
        """
        Recibe los objetos entry_n,entry_l y entry_m. 
        se guardan los valores recibidos en formato de enteros. 
        Se devuelven los 3 numeros en formato de tupla
        """
        valores=[]
        for entry in (entry_n,entry_l,entry_m):
            if entry is not None:
                texto=entry.text().strip()
                if texto=="":
                    valores.append(None)
                else:
                    valores.append(int(texto))
        return tuple(valores)