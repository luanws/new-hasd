from PyQt5.QtCore import QSize, Qt, QUrl
from PyQt5.QtGui import QFont
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (QHBoxLayout, QPushButton, QSlider, QStatusBar,
                             QStyle, QVBoxLayout, QWidget)


class VideoPlayerWidget(QWidget):

    def __init__(self, parent=None):
        super(VideoPlayerWidget, self).__init__(parent)

        self.media_player = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        video_widget = QVideoWidget()

        self.playButton = QPushButton()
        self.playButton.setEnabled(False)
        self.playButton.setFixedHeight(24)
        self.playButton.setIconSize(QSize(16, 16))
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playButton.clicked.connect(self.play)

        self.positionSlider = QSlider(Qt.Horizontal)
        self.positionSlider.setRange(0, 0)
        self.positionSlider.sliderMoved.connect(self.set_position)

        self.statusBar = QStatusBar()
        self.statusBar.setFont(QFont("Noto Sans", 8))
        self.statusBar.setFixedHeight(14)

        controlLayout = QHBoxLayout()
        controlLayout.setContentsMargins(0, 0, 0, 0)
        controlLayout.addWidget(self.playButton)
        controlLayout.addWidget(self.positionSlider)

        layout = QVBoxLayout()
        layout.addWidget(video_widget)
        layout.addLayout(controlLayout)
        layout.addWidget(self.statusBar)

        self.setLayout(layout)

        self.media_player.setVideoOutput(video_widget)
        self.media_player.stateChanged.connect(self.media_state_changed)
        self.media_player.positionChanged.connect(self.position_changed)
        self.media_player.durationChanged.connect(self.duration_changed)
        self.media_player.error.connect(self.handle_error)
        self.statusBar.showMessage("Ready")

    def play_video(self, video_path: str):
        self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(video_path)))
        self.playButton.setEnabled(True)
        self.statusBar.showMessage(video_path)
        self.play()

    def play(self):
        if self.media_player.state() == QMediaPlayer.PlayingState:
            self.media_player.pause()
        else:
            self.media_player.play()

    def media_state_changed(self, state):
        if self.media_player.state() == QMediaPlayer.PlayingState:
            self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))

    def position_changed(self, position):
        self.positionSlider.setValue(position)

    def duration_changed(self, duration):
        self.positionSlider.setRange(0, duration)

    def set_position(self, position):
        self.media_player.setPosition(position)

    def handle_error(self):
        self.playButton.setEnabled(False)
        self.statusBar.showMessage("Error: " + self.media_player.errorString())
