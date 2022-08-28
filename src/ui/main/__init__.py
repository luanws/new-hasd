
import os
from typing import List

from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow
from src.services import VideoService
from src.ui.main.window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.setWindowIcon(QtGui.QIcon('icon.ico'))

        self.video_service = VideoService('data')

        self.searchVideoLineEdit.textChanged.connect(self.search_video)
        self.videoListWidget.itemDoubleClicked.connect(self.play_video)

    def search_video(self):
        search_text = self.searchVideoLineEdit.text()
        videos = self.video_service.search_videos(search_text)
        self.show_videos(videos)

    def show_videos(self, videos: List[str]):
        self.videoListWidget.clear()
        for video in videos:
            self.videoListWidget.addItem(video)

    def play_video(self, video: str):
        pass
