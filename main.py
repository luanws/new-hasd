import sys

from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QSplashScreen

from src.ui.main import MainWindow


def main():
    app = QApplication(sys.argv)

    splash_screen = QSplashScreen(QPixmap('res/img/splash.png'))
    splash_screen.show()

    main_window = MainWindow()
    main_window.showMaximized()

    splash_screen.close()

    app.exec()


def except_hook(cls, exception, traceback):
    message_box = QtWidgets.QMessageBox()
    message_box.setIcon(QtWidgets.QMessageBox.Critical)
    message_box.setText("Error")
    message_box.setInformativeText(str(exception))
    message_box.setWindowTitle("Error")
    message_box.exec_()


if __name__ == '__main__':
    sys.excepthook = except_hook
    main()
