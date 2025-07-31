from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout


def boton_menu(text, on_click, font_size=22, width=None, height=None,padding_v=35, padding_h=80):
    style = (
        f"background-color: #02023A;"
        f"color: white;"
        f"font-weight: bold;"
        f"font-size: {font_size}px;"
        f"padding: {padding_v}px {padding_h}px;"
        "border-radius: 7px;"
    )
    btn = QPushButton(text)
    btn.setStyleSheet(style)
    if width and height:
        btn.setFixedSize(width, height)
    elif width:
        btn.setFixedWidth(width)
    elif height:
        btn.setFixedHeight(height)
    btn.clicked.connect(on_click)
    return btn