from PyQt5 import QtWidgets


class Container(QtWidgets.QVBoxLayout):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setContentsMargins(0, 0, 0, 0)
