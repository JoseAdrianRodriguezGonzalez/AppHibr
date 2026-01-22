import webbrowser
import os
from PyQt5.QtWidgets import QPushButton

def boton_url(valor, on_click=None, url=None, font_size=15, width=180, height=45, padding_v=5, padding_h=5):
    """
    boton con enlace
    """
   
    style = f"""
        QPushButton {{
            background-color: #02023A;
            color: white;
            font-size: {font_size}px;
            border-radius: 7px;
            border: 2px solid #02023A;
            padding: {padding_v}px {padding_h}px;
        }}
        QPushButton:hover {{
            background-color: #0F0F85;
            border: 2px solid #7777FF;
            color: #FFFFFF;

        }}
        QPushButton:pressed {{
            background-color: #000015;
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