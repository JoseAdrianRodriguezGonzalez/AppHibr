from PyQt5.QtWidgets import QComboBox
from PyQt5.QtCore import Qt

# def combobox(items, on_change=None):
#     """
#     Crea y retorna un QComboBox super estilizado.
#     Solo debes cambiar los items y, opcionalmente, el on_change.

#     Parámetros:
#     - items: lista de strings a mostrar como opciones.
#     - on_change: función/callback ejecutada al cambiar la selección (opcional).
#     """
#     style = """
#     QComboBox {
#         background-color: #02023A;
#         color: #E6E6FC;
#         font-family: 'Inter';
#         font-weight: bold;
#         font-size: 16px;
#         padding: 4px 10px;
#         border-radius: 12px;
#         padding: 16px 48px;
#         min-height: 48px;
#         min-width: 200px;
#         qproperty-alignment: 'AlignCenter';
#     }
#     QComboBox::drop-down {
#         border: none;
#         background: transparent;
#         width: 0px;
#         height: 0px;
#     }
#     QComboBox::down-arrow {
#         image: none;
#         border: none;
#         width: 0px;
#         height: 0px;
#     }
#     QComboBox QAbstractItemView {
#         background-color: #02023A;
#         color: #2A2A70;
#         border-radius: 12px;
#         selection-background-color: #01012B;
#         padding: 4px 0px;
#         font-size: 16px;
#     }
#     QComboBox:item {
#         min-height: 32px;
#         text-align: center;
#     }
#     QComboBox QScrollBar:vertical {
#         width: 8px;
#         margin: 2px 0 2px 0;
#     }
#     """
#     combo = QComboBox()
#     combo.setStyleSheet(style)
#     combo.addItems(items)
#     combo.setEditable(False)  # No editable, así texto siempre centrado
#     # Forzar alineación centrada en cada ítem
#     combo.setInsertPolicy(QComboBox.NoInsert)
#     for i in range(combo.count()):
#         combo.setItemData(i, Qt.AlignCenter, Qt.TextAlignmentRole)
#     if on_change:
#         combo.currentIndexChanged.connect(on_change)
#     return combo


def combobox(items, on_change=None):
    """
    Crea y retorna un QComboBox estilizado.
    Solo debes cambiar los items y, si quieres, el on_change.

    parámetros:
    - items: lista de strings para mostrar como opciones.
    - on_change: función/callback (opcional) cuando cambia la opción.
    """
    style = """
    QComboBox {
        background-color: #02023A;
        color: #EFFFFF;
        font-family: 'Inter';
        font-weight: bold;
        font-size: 16px;
        border: none;
        border-radius: 12px;
        padding: 10px 20px;
        min-width: 100px;
        qproperty-alignment: 'AlignCenter';
    }
    QComboBox::drop-down {
        border: none;
        width: 20px;
    }
    QComboBox QAbstractItemView {
        background-color: #01012B;
        color: #EFFFFF;
        border-radius: 12px;
        selection-background-color: #01012B;
        font-size: 18px;
    }
    QComboBox::down-arrow {
        image: url(utils/downarrow.svg);
        width: 24px;
        height: 24px;
        margin: 4px 16px 4px 0;
    }
    QComboBox:item {
        min-height: 32px;
        text-align: center;
    }
    QComboBox QScrollBar:vertical {
        width: 16px;
        margin: 2px 0 2px 0;
    }
    """
    combo = QComboBox()
    combo.setStyleSheet(style)
    combo.addItems(items)
    combo.setFixedWidth(150)  # Ajusta el ancho real del control
    combo.setEditable(False)
    # for i in range(combo.count()):
    #     combo.setItemData(i, Qt.AlignCenter, Qt.TextAlignmentRole)
    if on_change:
        combo.currentIndexChanged.connect(on_change)
    return combo

