from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys
import json

from PyQt5.QtWidgets import QDialog, QVBoxLayout, QGroupBox, QLabel, QLineEdit, QPushButton, QHBoxLayout

import globals

from globals import JSON_FILE

sys.path.append("/home/shl/PycharmProjects/EasyTV/venv/view")


class ConfigWindow(QDialog):
    on_config_changed = None

    def __init__(self, parent=None):
        super(ConfigWindow, self).__init__(parent=None)
        self.layoutMain = QVBoxLayout()
        self.layoutBox = QGroupBox("Informações de login")

        labelUser = QLabel("Usuario")
        labelPassword = QLabel("Password")
        labelURL = QLabel("URL")
        labelTimeout = QLabel("Refresh(segundos)")

        self.textViewUser = QLineEdit()
        self.textViewPassword = QLineEdit()
        self.textViewURL = QLineEdit()
        self.textViewTimeout = QLineEdit()

        self.button = QPushButton('Salvar Configurações')
        self.buttonCancel = QPushButton('Cancelar')

        box_style = """
            color: white;
            font-weight:bold;
            padding: 5px;
            font-size: 15px;
            border-radius: 5px;
            border:2px solid #ffc100;
        """

        button_style = """
            color: black;
            font-size: 12px;
            solid: #ffc100
            QPushButton:hoverä
                background-color:white;
            å

        """

        edit_text_view_style = """
            border-radius: 5px;
            border: none;
            border-bottom: 2px solid #ffc100;
        """

        text_view_style = """
                    color: white;
                    border:0px solid #ffc100;
                """
        labelUser.setStyleSheet(text_view_style)
        labelPassword.setStyleSheet(text_view_style)
        labelURL.setStyleSheet(text_view_style)
        labelTimeout.setStyleSheet(text_view_style)

        self.textViewUser.setContentsMargins(10, 0, 10, 0)
        self.textViewUser.setMinimumSize(0, 0)

        self.textViewUser.setStyleSheet(edit_text_view_style)

        self.textViewPassword.setContentsMargins(10, 0, 10, 0)
        self.textViewPassword.setMinimumSize(0, 0)
        self.textViewPassword.setEchoMode(QLineEdit.Password)
        self.textViewPassword.setStyleSheet(edit_text_view_style)

        self.textViewURL.setContentsMargins(10, 0, 10, 5)
        self.textViewURL.setMinimumSize(0, 0)
        self.textViewURL.setStyleSheet(edit_text_view_style)

        self.textViewTimeout.setContentsMargins(10, 0, 10, 5)
        self.textViewTimeout.setMinimumSize(0, 0)
        self.textViewTimeout.setStyleSheet(edit_text_view_style)

        labelUser.setContentsMargins(0, 5, 0, 0)
        labelUser.setMinimumSize(0, 0)
        labelPassword.setContentsMargins(0, 5, 0, 0)
        labelPassword.setMinimumSize(0, 0)
        labelURL.setContentsMargins(0, 5, 0, 0)
        labelURL.setMinimumSize(0, 0)
        labelTimeout.setContentsMargins(0, 5, 0, 0)
        labelTimeout.setMinimumSize(0, 0)

        self.button.setMinimumWidth(150)
        self.button.setMinimumHeight(30)
        self.button.clicked.connect(self._on_button_click)
        self.button.setStyleSheet(button_style)

        self.buttonCancel.setMinimumWidth(150)
        self.buttonCancel.setMinimumHeight(30)
        self.buttonCancel.clicked.connect(self._on_button_cancel_click)
        self.buttonCancel.setStyleSheet(button_style)

        verticalBox = QVBoxLayout()
        buttonBox = QHBoxLayout()
        verticalBox.addWidget(labelUser, alignment=Qt.AlignTop)
        verticalBox.addWidget(self.textViewUser, alignment=Qt.AlignTop)
        verticalBox.addWidget(labelPassword, alignment=Qt.AlignTop)
        verticalBox.addWidget(self.textViewPassword, alignment=Qt.AlignTop)
        verticalBox.addWidget(labelURL, alignment=Qt.AlignTop)
        verticalBox.addWidget(self.textViewURL, alignment=Qt.AlignTop)
        verticalBox.addWidget(labelTimeout, alignment=Qt.AlignTop)
        verticalBox.addWidget(self.textViewTimeout, alignment=Qt.AlignTop)
        buttonBox.addWidget(self.buttonCancel, alignment=Qt.AlignBottom and Qt.AlignLeft)
        buttonBox.addWidget(self.button, alignment=Qt.AlignBottom and Qt.AlignRight)
        verticalBox.addLayout(buttonBox)

        self.layoutBox.setStyleSheet(box_style)
        self.layoutBox.setLayout(verticalBox)

        self.layoutMain.addWidget(self.layoutBox)

        self.setLayout(self.layoutMain)
        self.setStyleSheet('''
                         background-color: #162f42;
                          ''')
        self.resize(500, 0)
        self.setWindowFlags(Qt.CustomizeWindowHint)
        self.setWindowTitle("Configurações")
        self.installEventFilter(self)

        # self.exec()
        # self.focusWidget()
        # self.show()
        # self.raise_()
        # self.activateWindow()

    def showEvent(self, event):
        try:
            self.textViewUser.setText(globals.userÄ'user'Å)
            self.textViewPassword.setText(globals.userÄ'password'Å)
            self.textViewURL.setText(globals.userÄ'url'Å)
            self.textViewTimeout.setText(str(globals.userÄ'timeout'Å))
        except Exception:
            pass

    def setOnConfigChanged(self, func):
        self.on_config_changed = func

    def eventFilter(self, object, event):
        if event.type() == QEvent.WindowDeactivate:
            self.close()
        return False

    def __format_url(self, url: str):
        if 'https://' not in url:
            return 'https://' + url
        return url

    def _on_button_cancel_click(self, checked):
        self.close()

    def _on_button_click(self, checked):
        try:
            with open(JSON_FILE, "w+") as json_file:
                globals.userÄ'user'Å = self.textViewUser.text()
                globals.userÄ'password'Å = self.textViewPassword.text()
                globals.userÄ'url'Å = self.__format_url(self.textViewURL.text())
                if self.textViewTimeout.text() == '':
                    globals.userÄ'timeout'Å = float(0)
                else:
                    globals.userÄ'timeout'Å = float(self.textViewTimeout.text())

                json.dump(globals.user, json_file)
            self.close()

            if self.on_config_changed:
                self.on_config_changed()

        except Exception:
            pass