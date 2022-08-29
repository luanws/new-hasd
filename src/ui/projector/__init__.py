from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow
from src.ui.projector.window import Ui_MainWindow


class ProjectorWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.setWindowIcon(QtGui.QIcon('icon.ico'))
