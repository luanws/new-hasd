from typing import List

from PyQt5 import QtGui
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QShortcut
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
        self.searchVideoLineEdit.returnPressed.connect(self.play_first_video_in_list)
        self.videoListWidget.itemDoubleClicked.connect(self.play_clicked_video)

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
        videos = self.video_service.search_videos(search_text)
        self.show_videos(videos)

    def show_videos(self, videos: List[str]):
        self.videoListWidget.clear()
        for video in videos:
            self.videoListWidget.addItem(video)

    def play_video(self, video: str):
        screen = QApplication.screens()[-1]
        screen = QApplication.screens()[-1]
        self.projector_window.show()
        self.projector_window.windowHandle().setScreen(screen)
        self.projector_window.showFullScreen()
        self.projector_window.play_video(self.video_service.get_video_path_from_video(video))

    def play_first_video_in_list(self):
        first_item = self.videoListWidget.item(0)
        if first_item:
            video = first_item.text()
            self.play_video(video)

    def play_clicked_video(self):
        video = self.videoListWidget.currentItem().text()
        self.play_video(video)
