from typing import List

from PyQt5 import QtGui
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication, QMainWindow
from src.services import VideoService
from src.ui.main.window import Ui_MainWindow
from src.ui.projector import ProjectorWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.setWindowIcon(QtGui.QIcon('icon.ico'))

        self.projector_window = ProjectorWindow()

        self.video_service = VideoService('data')

        self.searchVideoLineEdit.textChanged.connect(self.search_video)
        self.videoListWidget.itemDoubleClicked.connect(self.play_video)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        application = QCoreApplication.instance()
        if application:
            application.quit()

    def search_video(self):
        search_text = self.searchVideoLineEdit.text()
        videos = self.video_service.search_videos(search_text)
        self.show_videos(videos)

    def show_videos(self, videos: List[str]):
        self.videoListWidget.clear()
        for video in videos:
            self.videoListWidget.addItem(video)

    def play_video(self, video: str):
        screen = QApplication.screens()[-1]
        self.projector_window.show()
        self.projector_window.windowHandle().setScreen(screen)
        self.projector_window.showFullScreen()
