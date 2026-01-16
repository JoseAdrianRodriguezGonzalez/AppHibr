from PyQt5.QtWidgets import QPushButton

def boton_menu(valor, on_click, font_size=22, width=None, height=None, padding_v=35, padding_h=80):
    # Definimos el estilo completo incluyendo los estados hover y pressed
    style = f"""
        QPushButton {{
            background-color: #02023A;
            color: white;
            font-weight: bold;
            font-size: {font_size}px;
            padding: {padding_v}px {padding_h}px;
            border-radius: 7px;
            border: 2px solid #4B4BFF; /* Borde definido para mejor estética */
        }}
        QPushButton:hover {{
            background-color: #0F0F85; /* Azul más claro al pasar el mouse */
            border: 2px solid #7777FF; /* Borde más brillante */
            color: #FFFFFF;
        }}
        QPushButton:pressed {{
            background-color: #000015; /* Azul muy oscuro al hacer clic */
            border: 2px solid #02023A; /* Borde sutil */
        }}
    """
    
    btn = QPushButton(valor)
    btn.setStyleSheet(style)
    
    # Lógica para dimensiones (tuya original)
    if width and height:
        btn.setFixedSize(width, height)
    elif width:
        btn.setFixedWidth(width)
    elif height:
        btn.setFixedHeight(height)
        
    btn.clicked.connect(on_click)
    return btn