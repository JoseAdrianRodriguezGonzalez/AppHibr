import webbrowser
import os
from PyQt5.QtWidgets import QPushButton

def boton_url(valor, on_click=None, url=None, font_size=22, width=200, height=50, padding_v=30, padding_h=30):
    """
    Crea un botón con texto
    """
   
    style = f"""
        QPushButton {{
            background-color: #02023A;
            color: white;
            border: 1px solid #4B4BFF;
            padding: 5px;
            border-radius: 5px;
            font-family: 'Inter';
            min-width: 200px;
        }}
        QPushButton:hover {{
            background-color: #0F0F85;
            border: 2px solid #7777FF;
        }}
        QPushButton:pressed {{
            background-color: #4B4BFF;
            border: 2px solid #02023A;
        }}
    """
    
    btn = QPushButton(valor)
    btn.setStyleSheet(style)
    


    def handle_click():
        if url:
            webbrowser.open(url)

    btn.clicked.connect(handle_click)
    
    return btn