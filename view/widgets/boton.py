from PyQt5.QtWidgets import QPushButton

def boton_menu(valor, on_click, font_size=22, width=None, height=None, padding_v=30, padding_h=30):
    style = f"""
        QPushButton {{
            background-color: #02023A;
            color: white;
            font-weight: bold;
            font-size: {font_size}px;
            padding: {padding_v}px {padding_h}px;
            border-radius: 7px;
            border: 2px solid #02023A;
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
    
    if width and height:
        btn.setFixedSize(width, height)
    elif width:
        btn.setFixedWidth(width)
    elif height:
        btn.setFixedHeight(height)
        
    btn.clicked.connect(on_click)
    return btn