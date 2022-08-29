from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow
from src.ui.projector.window import Ui_MainWindow

from .video_player_widget import VideoPlayerWidget


class ProjectorWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.setWindowIcon(QtGui.QIcon('icon.ico'))

        self.video_player_widget = VideoPlayerWidget()
        self.centralWidget().layout().addWidget(self.video_player_widget)

    def play_video(self, video_path: str):
        print(video_path)
        self.video_player_widget.play_video(video_path)
