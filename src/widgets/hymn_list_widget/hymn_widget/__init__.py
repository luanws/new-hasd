from PyQt5 import QtWidgets
from src.models.hymn import Hymn

from .container import Container
from .hymn_name_label import HymnNameLabel


class HymnWidget(QtWidgets.QWidget):
    hymn: Hymn

    def __init__(self, parent: QtWidgets.QWidget = None, *, hymn: Hymn):
        super(HymnWidget, self).__init__(parent)

        self.hymn = hymn

        self.container = Container(self)
        self.hymn_name_label = HymnNameLabel(text=hymn.name)

        self.container.addWidget(self.hymn_name_label)

        self.setLayout(self.container)
