import PyQt5
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import sys

# sys.path.append("/home/shl/PycharmProjects/EasyTV/venv/view")

from model.AdminDb import AdminDb
from .ConfigWindow import ConfigWindow

import sqlite3


class LoginWindow(QDialog):
    def __init__(self, parent=None):
        super(LoginWindow, self).__init__()
        self.centralWidget = QWidget(self)
        self.windowLayout = QVBoxLayout()
        self.labelLogin = QLabel("Usuário:")
        self.labelPass = QLabel("Senha:")
        self.editTextLogin = QLineEdit()
        self.editTextPass = QLineEdit()
        self.buttonConfirm = QPushButton("Confirmar")

        self.editTextPass.setEchoMode(QLineEdit.Password)

        self.buttonConfirm.clicked.connect(self.on_button_confirm_clicked)

        self.windowLayout.addWidget(self.labelLogin)
        self.windowLayout.addWidget(self.editTextLogin)
        self.windowLayout.addWidget(self.labelPass)
        self.windowLayout.addWidget(self.editTextPass)
        self.windowLayout.addWidget(self.buttonConfirm)

        # self.setFixedWidth(400)
        # self.setFixedHeight(300)
        self.setWindowTitle("Configurações")
        self.setLayout(self.windowLayout)
        self.exec()
        self.show()

    def on_button_confirm_clicked(self):

        adminDb = AdminDb()
        exists = False
        for line in adminDb.select_admins():
            print(lineÄ1Å)
            print(self.editTextLogin.text().__str__())
            print(lineÄ2Å)
            print(self.editTextPass.text().__str__())

            if lineÄ1Å == self.editTextLogin.text().__str__():
                if lineÄ2Å == self.editTextPass.text().__str__():
                    exists = True
        if exists:
            ConfigWindow()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Usuario não existe")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

        adminDb.close()