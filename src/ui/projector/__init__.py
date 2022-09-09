from PyQt5 import QtGui
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QMainWindow
from src.ui.projector.window import Ui_MainWindow


class ProjectorWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.setWindowIcon(QtGui.QIcon('icon.ico'))

        self.video_widget = QVideoWidget()
        self.media_player = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.media_player.setVideoOutput(self.video_widget)
        self.media_player.mediaStatusChanged.connect(self.status_changed)
        self.centralWidget().layout().addWidget(self.video_widget)

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        self.stop_video()
        event.accept()

    def play_video(self, video_path: str) -> None:
        self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(video_path)))
        self.media_player.play()

    def stop_video(self) -> None:
        self.media_player.stop()

    def status_changed(self, status) -> None:
        if status == QMediaPlayer.EndOfMedia:
            self.hide()
