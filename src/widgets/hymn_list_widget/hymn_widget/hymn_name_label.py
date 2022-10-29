from PyQt5 import QtWidgets


class HymnNameLabel(QtWidgets.QLabel):
    def __init__(self, parent=None, *, text: str):
        super().__init__(parent)

        self.setText(text)
        self.setWordWrap(True)
        self.setStyleSheet('''
            font-size: 12px;
            color: #fff;
        ''')
        self.setFixedHeight(100)
