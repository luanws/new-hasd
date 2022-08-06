from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(709, 578)
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
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(16, 8, 16, 16)
        self.verticalLayout.setObjectName("verticalLayout")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setMaximumSize(QtCore.QSize(16777215, 40))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout.addWidget(self.plainTextEdit)
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
