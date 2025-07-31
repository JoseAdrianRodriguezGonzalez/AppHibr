from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtGui import QIntValidator
from PyQt5.QtCore import Qt

def number(value=None, on_change=None):
    style = """
    QLineEdit {
        background-color: #02023A;
        color: #EFFFFF;
        font-family: 'Inter';
        font-weight: bold;
        font-size: 20px;
        padding: 12px 20px;
        border-radius: 13px;
        min-width: 50px;
        qproperty-alignment: AlignCenter;
    }
    QLineEdit:focus { outline: none;}
    QLineEdit::placeholder { color: #EFFFFF; }
    """
    entry = QLineEdit()
    entry.setStyleSheet(style)
    entry.setText(str(value))
    entry.setFixedSize(80, 50)
    entry.setAlignment(Qt.AlignCenter)
    # Solo números si quieres (puedes quitar esto si necesitas texto)
    entry.setValidator(QIntValidator())
    if on_change:
        entry.textChanged.connect(on_change)
    return entry