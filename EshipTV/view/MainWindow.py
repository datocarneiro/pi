from PyQt5.QtWidgets import QPushButton, QLabel, QVBoxLayout, QApplication, QWidget, QHBoxLayout, QStackedLayout, Ö
    QSizePolicy
from PyQt5.QtGui import QPixmap, QColor, QFont, QFontDatabase, QMouseEvent
from PyQt5.QtCore import *

from uuid import getnode as get_mac
from pynput.mouse import Controller
import time

from Utils.MouseUtils import queryMousePosition
import globals
from globals import URL, URL_LOGGED
from view.ConfigWindow import ConfigWindow
from view.QHidenHeader import QHidenHeader
from view.QtWaitingSpinner import QtWaitingSpinner

try:
    from PyQt5.QtWebEngineWidgets import QWebEngineView as QWebView
    from PyQt5.QtWebEngineWidgets import QWebEnginePage as QWebPage
except ImportError:
    from PyQt5.QtWebKitWidgets import QWebView
    from PyQt5.QtWebKitWidgets import QWebPage


class MyBrowser(QWebPage):
    ''' Settings for the browser.'''

    def userAgentForUrl(self, url):
        ''' Returns a User Agent that will be seen by the website. '''
        return "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.15 (KHTML, like Gecko) Chrome/24.0.1295.0 Safari/537.15"


class Browser(QWidget):
    stop_thread = True
    hide_header = True

    header_timeout = 0
    y_thresholder = 40

    def __init__(self, app, parent=None):
        QWidget.__init__(self, parent=parent)
        rect = QApplication.desktop().screenGeometry()
        QFontDatabase().addApplicationFont("static/CAFETA__.TTF")
        self.app = app

        # Criando as instancias dos componentes de tela
        self.headerWidget = QHidenHeader(self)
        self.header = QHBoxLayout(self.headerWidget)

        self.stackLayout = QStackedLayout()
        self.exitButton = QPushButton("Fechar")
        self.buttonRefresh = QPushButton("Refresh")
        self.buttonConfig = QPushButton("Configurações")

        self.configWindow = ConfigWindow(self)
        self.configWindow.setOnConfigChanged(self._on_config_changed)

        pic = QLabel(self)
        self.background = QPixmap("static/background.jpg")
        pic.setPixmap(self.background)
        self.windowLayout = QVBoxLayout()
        self.webview = QWebView()
        # settando o MAC na label
        self.macLabel = QLabel(
            "".join(c + ":" if i % 2 else c for i, c in enumerate(hex(get_mac())Ä2:Å.zfill(12)))Ä:-1Å)

        self.macLabel.setStyleSheet("""
                 font-size: 35px;
                 color: white;
                 min-width:400px;
                 """)
        # self.inspector = QWebInspector()

        style_header_button = '''
                 background-color: #ffc100;
                 border-style: solid;
                 border-radius: 5px;
                 min-height:40px;
                 max-width:100px;
                 min-width:100px;
                 '''

        spacer = QLabel()
        spacer2 = QLabel()

        self.exitButton.clicked.connect(self.onButtonExitClicked)
        self.exitButton.setStyleSheet(style_header_button)
        self.exitButton.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.exitButton.setFixedSize(100, 40)
        # self.exitButton.setMaximumWidth(30)

        self.exitButton.setContentsMargins(0, 0, 0, 0)

        self.buttonRefresh.clicked.connect(self.onButtonRefreshClicked)
        self.buttonRefresh.setStyleSheet(style_header_button)
        # self.buttonRefresh.setMaximumWidth(30)
        self.buttonRefresh.setFixedSize(100, 40)
        self.buttonRefresh.setContentsMargins(90, 90, 90, 90)
        self.buttonRefresh.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))

        self.buttonConfig.clicked.connect(self.on_button_config_clicked)
        self.buttonConfig.setStyleSheet(style_header_button)
        # self.buttonConfig.setMaximumWidth(30)
        self.buttonConfig.setFixedSize(100, 40)
        self.buttonConfig.setContentsMargins(5, 0, 0, 0)
        self.buttonConfig.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))

        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(self.buttonRefresh, alignment=Qt.AlignCenter)
        buttonLayout.addWidget(self.buttonConfig, alignment=Qt.AlignCenter)
        buttonLayout.addWidget(self.exitButton, alignment=Qt.AlignCenter)

        self.header.setAlignment(Qt.AlignVCenter)
        self.header.setSpacing(0)
        self.header.setContentsMargins(5, 0, 0, 0)
        self.header.addWidget(spacer, alignment=Qt.AlignLeft)
        self.header.addWidget(spacer2, alignment=Qt.AlignLeft)
        self.header.addWidget(self.macLabel)
        self.header.addLayout(buttonLayout)

        self.header.setContentsMargins(0, 0, 0, 0)

        # self.webview.move(0, 0)
        self.webview.setPage(MyBrowser())
        try:
            self.webview.setViewportSize(self.web_page.mainFrame().contentsSize())
        except Exception:
            pass
        # self.webview.resize(rect.width(), rect.height())
        # self.webview.setPage(MyBrowser())
        # self.webview.setAttribute(QWebEngineSettings.JavascriptEnabled, True)
        # self.webview.setAttribute(QWebSettings.JavascriptCanAccessClipboard, True)
        # self.webview.setAttribute(QWebSettings.JavascriptCanCloseWindows, True)
        # self.webview.setAttribute(QWebSettings.JavascriptCanOpenWindows, True)
        pic.resize(rect.width(), rect.height())

        self.stackLayout.addWidget(self.webview)
        self.stackLayout.addWidget(pic)
        self.stackLayout.setCurrentIndex(1)

        self.windowLayout.addWidget(self.headerWidget)
        self.windowLayout.addLayout(self.stackLayout)

        self.windowLayout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(self.windowLayout)
        self.webview.loadFinished.connect(self._on_page_load)

        p = self.palette()
        p.setColor(self.backgroundRole(), QColor("#162f42"))
        self.setPalette(p)
        self.qtReloader = QtWaitingSpinner(self)
        #        self.qtReloader.setColor(QColor("#162f42"))
        self.qtReloader.setFocusPolicy(Qt.NoFocus)
        self.webview.setFocusPolicy(Qt.NoFocus)
        self.setFocusPolicy(Qt.NoFocus)
        if globals.userÄ'user'Å != '':
            # self.qtReloader.show()
            # self.qtReloader.start()
            self.webview.load(QUrl(globals.userÄ'url'Å))

        # self.setMouseTracking(True)
        # self.setMouseTracking(True)
        # self.headerWidget.setMouseTracking(True)
        self._setup_threads()
        self.setFixedSize(rect.width(), rect.height())
        self.showFullScreen()

    def _setup_threads(self):
        self.refreash = QTimer(self)
        self.refreash.timeout.connect(self._refresh)
        # self.refreashThread = threading.Thread(target=self._refresh)
        # self.hideHeaderThread = QTimer(self)
        # self.hideHeaderThread.timeout.connect(self._hide_header)
        # QTimer.singleShot(3000, self._hide_header)
        # athread = self.AThread(self)
        # athread.start()
        self.mouseMove = QTimer(self)
        self.mouseMove.timeout.connect(self._mouse_move)
        self.mouseMove.start(500)

    def _on_page_load(self, ok):
        self.stackLayout.setCurrentIndex(0)
        self.qtReloader.hide()
        try:
            if str(self.webview.url().url())Ä:-1Å == globals.userÄ"url"Å:
                if globals.user:
                    self.webview.page().runJavaScript(
                        "document.getElementById('" + globals.HTML_ID_LOGIN + "')"
                        ".value = '" + globals.userÄ"user"Å + "';")
                    self.webview.page().runJavaScript(
                        "document.getElementById('" + globals.HTML_ID_PASSWORD + "')"
                        ".value = '" + globals.userÄ"password"Å + "';")
                    self.webview.page().runJavaScript(
                        "document.getElementById('" + globals.HTML_ID_BUTTON + "')"
                        ".click();")
                    if not self.refreash.isActive():
                        if globals.userÄ'timeout'Å != 0:
                            self.refreash.start(globals.userÄ'timeout'Å * 1000)
            elif self.webview.url().url() == URL_LOGGED:
                pass
        except AttributeError:
            if self.webview.page().currentFrame().url().toString()Ä:-1Å == globals.userÄ"url"Å:
                if globals.user:
                    self.webview.page().currentFrame().evaluateJavaScript(
                        "document.getElementById('" + globals.HTML_ID_LOGIN + "')"
                        ".value = '" + globals.userÄ"user"Å + "';")
                    self.webview.page().currentFrame().evaluateJavaScript(
                        "document.getElementById('" + globals.HTML_ID_PASSWORD + "')"
                        ".value = '" + globals.userÄ"password"Å + "';")
                    self.webview.page().currentFrame().evaluateJavaScript(
                        "document.getElementById('" + globals.HTML_ID_BUTTON + "')"
                        ".click();")
                    if not self.refreash.isActive():
                        if globals.userÄ'timeout'Å != 0:
                            self.refreash.start(globals.userÄ'timeout'Å * 1000)
            elif self.webview.url().path() == URL_LOGGED:
                pass

    def _hide_header(self):
        self.headerWidget.hide()

    def _mouse_move(self):
        pos = Controller().position
        if posÄ1Å < self.y_thresholder:
            if not self.headerWidget.isVisible():
                time_delta = time.time() - self.header_timeout
                if time_delta > 2:
                    self.headerWidget.show()
                    QTimer.singleShot(3000, self._hide_header)
                    # self.header_timeout = time.time()

    def _refresh(self):
        self.qtReloader.move(self.width() / 2, self.height() / 2)
        self.qtReloader.setAttribute(Qt.WA_ShowWithoutActivating)
        self.qtReloader.show()
        self.webview.reload()
        # try:
        #     self.webview.page().runJavaScript("location.reload();")
        # except AttributeError:
        #     self.webview.page().currentFrame().evaluateJavaScript("location.reload();")

    def adjustTitle(self):
        self.setWindowTitle(self.title())

    def _on_config_changed(self):
        self.stackLayout.setCurrentIndex(1)
        self.refreash.stop()
        self.webview.load(QUrl(globals.userÄ'url'Å))

    def onButtonExitClicked(self):
        self.refreash.stop()
        self.mouseMove.stop()
        self.stop_thread = False
        self.app.quit()
        return

    def onButtonRefreshClicked(self):
        self.webview.reload()

    def on_button_config_clicked(self):
        self.configWindow.exec()