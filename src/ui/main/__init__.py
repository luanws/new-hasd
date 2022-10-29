from typing import List

from PyQt5 import QtGui
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QShortcut
from src.models.hymn import Hymn
from src.services.hymn_service import HymnService
from src.ui.main.window import Ui_MainWindow
from src.ui.projector import ProjectorWindow
from src.widgets.hymn_list_widget import HymnListWidget
from src.widgets.hymn_list_widget.hymn_widget import HymnWidget


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.setWindowIcon(QtGui.QIcon('icon.ico'))

        self.projector_window = ProjectorWindow()

        self.hymn_service = HymnService('data')

        self.searchVideoLineEdit.textChanged.connect(self.search_video)
        self.searchVideoLineEdit.returnPressed.connect(self.play_first_video_in_list)

        self.hymn_list_widget = HymnListWidget(list_widget=self.hymnListWidget)
        self.hymn_list_widget.list_widget.itemDoubleClicked.connect(self.play_clicked_video)

        self.configure_hot_keys()

    def configure_hot_keys(self) -> None:
        QShortcut(Qt.Key_Escape, self, self.projector_window.close)
        QShortcut(Qt.Key_Escape, self.projector_window, self.projector_window.close)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        application = QCoreApplication.instance()
        if application:
            application.quit()

    def search_video(self):
        search_text = self.searchVideoLineEdit.text()
        hymns = self.hymn_service.search_hymns(search_text)
        self.show_hymns(hymns)

    def show_hymns(self, hymns: List[Hymn]):
        self.hymn_list_widget.hymns = hymns

    def play_hymn(self, hymn: Hymn):
        screen = QApplication.screens()[-1]
        screen = QApplication.screens()[-1]
        self.projector_window.show()
        self.projector_window.windowHandle().setScreen(screen)
        self.projector_window.showFullScreen()
        self.projector_window.play_video(hymn.path)

    def play_first_video_in_list(self):
        hymn = self.hymn_list_widget.first_hymn()
        if hymn:
            self.play_hymn(hymn)

    def play_clicked_video(self):
        hymn = self.hymn_list_widget.current_hymn()
        self.play_hymn(hymn)
