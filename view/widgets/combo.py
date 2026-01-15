from PyQt5.QtWidgets import QComboBox

def combobox(items, on_change=None):
    """Crea un combobox con los items especificados."""
    style = """
    QComboBox {
        background-color: #02023A;
        color: white;
        font-family: 'Inter';
        font-weight: bold;
        font-size: 16px;
        padding: 8px;
        border-radius: 7px;
        min-width: 100px;
    }
    QComboBox:hover {
        background-color: #03034A;
    }
    QComboBox::drop-down {
        border: none;
        background-color: #02023A;
    }
    QComboBox::down-arrow {
        image: none;
        border-left: 5px solid transparent;
        border-right: 5px solid transparent;
        border-top: 5px solid white;
        margin-right: 10px;
    }
    QComboBox QAbstractItemView {
        background-color: #02023A;
        color: white;
        border: 1px solid #02023A;
        selection-background-color: #03034A;
        selection-color: white;
    }
    """

    combo = QComboBox()
    combo.setStyleSheet(style)
    combo.addItems(items)

    if on_change:
        combo.currentIndexChanged.connect(on_change)

    return combo