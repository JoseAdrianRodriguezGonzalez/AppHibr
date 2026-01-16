from PyQt5.QtWidgets import (QWidget, QLabel, QPushButton, QHBoxLayout, 
                             QVBoxLayout)
from PyQt5.QtCore import Qt, pyqtSignal

class CounterWidget(QWidget):
    valueChanged = pyqtSignal(int)

    def __init__(self, title="Title", min_val=0, max_val=10, initial_val=0, parent=None):
        super().__init__(parent)
        
        self.min_val = min_val
        self.max_val = max_val
        self.current_val = initial_val
        
        # Layout principal (vertical para Título y Controles)
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(10)
        self.title_label = QLabel(title)
        self.title_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.main_layout.addWidget(self.title_label)

        self.controls_layout = QHBoxLayout()
        self.controls_layout.setSpacing(20)

        self.btn_minus = QPushButton("-")
        self.btn_minus.setFixedSize(25, 25)
        self.btn_minus.setCursor(Qt.PointingHandCursor)
        
        # Etiqueta del Valor
        self.value_label = QLabel(str(self.current_val))
        self.value_label.setAlignment(Qt.AlignCenter)
        self.value_label.setMinimumWidth(30)
        
        # Botón Más
        self.btn_plus = QPushButton("+")
        self.btn_plus.setFixedSize(25, 25)
        self.btn_plus.setCursor(Qt.PointingHandCursor)

        self.controls_layout.addWidget(self.btn_minus)
        self.controls_layout.addWidget(self.value_label)
        self.controls_layout.addWidget(self.btn_plus)

        self.main_layout.addLayout(self.controls_layout)

        self.btn_minus.clicked.connect(self.decrement)
        self.btn_plus.clicked.connect(self.increment)

        self.setStyleSheet("""
            QWidget {
                color: #FFFFFF;
                font-family: 'Segoe UI', sans-serif;
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton {
                background-color: #02023A;
                border: 1px solid #4B4BFF;
                border-radius: 5px;
                font-weight: bold;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #05057E; /* Azul marino más claro para el hover */
                border: 1px solid #6666FF;
            }
            QPushButton:pressed {
                background-color: #000015; /* Azul casi negro para el pressed */
                border: 1px solid #02023A;
            }
            QLabel#valueLabel {
                font-size: 18px;
                font-weight: bold;
                background-color: #010122;
                border-radius: 5px;
                padding: 2px 10px;
            }
            QLabel#titleLabel {
                color: #AAAAAA;

            }
        """)
        self.value_label.setObjectName("valueLabel")
        self.title_label.setObjectName("titleLabel")

    def set_range(self, min_val, max_val):
        """Actualiza los limites permitidos"""
        self.min_val = min_val
        self.max_val = max_val
        if self.current_val < self.min_val:
            self.setValue(self.min_val)
        elif self.current_val > self.max_val:
            self.setValue(self.max_val)

    def setValue(self, value):
        """Establece un valor especifico manualmente"""
        if self.min_val <= value <= self.max_val:
            self.current_val = value
            self.update_display()
            self.valueChanged.emit(self.current_val)

    def get_value(self):
        """Retorna el valor actual"""
        return self.current_val

    def increment(self):
        if self.current_val < self.max_val:
            self.setValue(self.current_val + 1)

    def decrement(self):
        if self.current_val > self.min_val:
            self.setValue(self.current_val - 1)

    def update_display(self):
        self.value_label.setText(str(self.current_val))