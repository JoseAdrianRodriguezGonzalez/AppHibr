from PyQt5.QtWidgets import QComboBox
def combobox(items, on_change=None):
    """Crea un combobox con los items especificados."""


    style="""
      QComboBox {
            background-color: #02023A;
            color: white;
            border: 1px solid #4B4BFF;
            padding: 5px;
            border-radius: 5px;
            font-family: 'Inter';
            min-width: 200px;
            }
            QComboBox QAbstractItemView {
            background-color: #2D2D2D;
            color: white;
            selection-background-color: #4B4BFF;
            }
            QComboBox QAbstractItemView {
            background-color: #02023A;
            color: white;
            border: 1px solid #4B4BFF;
            selection-background-color: #4B4BFF;
            selection-color: white;
            border-radius: 4px;
            padding: 5px;
            }
             QComboBox:hover{
            background-color: #0F0F85;
            border: 2px solid #7777FF;
            }
    """
    combo = QComboBox()
    combo.setStyleSheet(style)
    combo.addItems(items)

    if on_change:
        combo.currentIndexChanged.connect(on_change)

    return combo