#!/usr/bin/env python
# -*- coding: utf-8 -*-


import time
from PyQt5.QtGui import QPixmap, QColor, QFont, QFontDatabase, QMouseEvent

from view.MainWindow import Browser

try:
    from PyQt5.QtWebEngineWidgets import QWebEngineView as QWebView
    from PyQt5.QtWebEngineWidgets import QWebEnginePage as QWebPage
except ImportError:
    from PyQt5.QtWebKitWidgets import QWebView
    from PyQt5.QtWebKitWidgets import QWebPage

import os
import json

from PyQt5.QtCore import *
# from PyQt4.QtWidgets import *

import sys
from pynput.mouse import Listener

from PyQt5.QtWidgets import QPushButton, QLabel, QVBoxLayout, QApplication, QWidget, QHBoxLayout, QStackedLayout

import globals
from Utils.MouseUtils import queryMousePosition
from globals import URL, URL_LOGGED, JSON_FILE
from view.ConfigWindow import ConfigWindow

from view.QHidenHeader import QHidenHeader

try:
    f = open(JSON_FILE, 'r+')
    globals.user = json.loads(f.read())
    f.close()
except Exception:
    f = open(JSON_FILE, 'w+')
    json.dump(globals.user, f)
    f.close()

if __name__ == "__main__":
    # win = BrowserView()
    # Gtk.main()

    app = QApplication(sys.argv)
    win = Browser(app)
    app.exec_()