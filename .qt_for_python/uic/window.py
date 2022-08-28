# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\GitHub\new-hasd\src\ui\main\window.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(805, 423)
        MainWindow.setStyleSheet("QPushButton {\n"
"    padding: 4px;\n"
"    background-color: transparent;\n"
"    border-radius: 16px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #ccc;\n"
"    color: white;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: #181818;\n"
"padding: 24px;")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(16, 8, 16, 16)
        self.verticalLayout.setSpacing(8)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setMaximumSize(QtCore.QSize(1024, 16777215))
        self.lineEdit.setStyleSheet("border-radius: 5px;\n"
"background-color: #212121;\n"
"text-align: center;\n"
"color: white;\n"
"padding: 12px 16px;\n"
"font-size: 20px;")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setMaximumSize(QtCore.QSize(1024, 16777215))
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionSair = QtWidgets.QAction(MainWindow)
        self.actionSair.setObjectName("actionSair")
        self.action_about = QtWidgets.QAction(MainWindow)
        self.action_about.setObjectName("action_about")
        self.actionVerificar_se_h_atualiza_es = QtWidgets.QAction(MainWindow)
        self.actionVerificar_se_h_atualiza_es.setObjectName("actionVerificar_se_h_atualiza_es")
        self.action_quit = QtWidgets.QAction(MainWindow)
        self.action_quit.setObjectName("action_quit")
        self.action_export_history = QtWidgets.QAction(MainWindow)
        self.action_export_history.setObjectName("action_export_history")
        self.action_advanced_search = QtWidgets.QAction(MainWindow)
        self.action_advanced_search.setObjectName("action_advanced_search")
        self.action_install_version = QtWidgets.QAction(MainWindow)
        self.action_install_version.setObjectName("action_install_version")
        self.action_remote = QtWidgets.QAction(MainWindow)
        self.action_remote.setObjectName("action_remote")
        self.action_projector_settings = QtWidgets.QAction(MainWindow)
        self.action_projector_settings.setObjectName("action_projector_settings")
        self.action_theme_settings = QtWidgets.QAction(MainWindow)
        self.action_theme_settings.setObjectName("action_theme_settings")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Projetor bíblico"))
        self.label.setText(_translate("MainWindow", "Hinário adventista do sétimo dia"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Pesquise aqui..."))
        self.actionSair.setText(_translate("MainWindow", "Sair"))
        self.action_about.setText(_translate("MainWindow", "Sobre"))
        self.actionVerificar_se_h_atualiza_es.setText(_translate("MainWindow", "Verificar se há atualizações"))
        self.action_quit.setText(_translate("MainWindow", "Sair"))
        self.action_export_history.setText(_translate("MainWindow", "Exportar histórico"))
        self.action_advanced_search.setText(_translate("MainWindow", "Pesquisa avançada"))
        self.action_install_version.setText(_translate("MainWindow", "Instalar versão"))
        self.action_remote.setText(_translate("MainWindow", "Controle remoto"))
        self.action_projector_settings.setText(_translate("MainWindow", "Projeção"))
        self.action_theme_settings.setText(_translate("MainWindow", "Temas"))