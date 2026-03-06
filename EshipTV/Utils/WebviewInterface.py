from abc import ABC, abstractmethod

__is_webview_defalut = True
try:
    from PyQt5.QtWebEngineWidgets import QWebEngineView as QWebView
    from PyQt5.QtWebEngineWidgets import QWebEnginePage as QWebPage
except ImportError:
    from PyQt5.QtWebKitWidgets import QWebView
    from PyQt5.QtWebKitWidgets import QWebPage

    __is_webview_defalut = False


class Webview(ABC, metaclass=QWebView):

    def __init__(self):
        super(Webview, self).__init__()

    @abstractmethod
    def runJavaScript(self, javascript):
        pass

    @abstractmethod
    def getUrl(self):
        pass

class MyBrowser(QWebPage):
    ''' Settings for the browser.'''

    def userAgentForUrl(self, url):
        ''' Returns a User Agent that will be seen by the website. '''
        return "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.15 (KHTML, like Gecko) Chrome/24.0.1295.0 Safari/537.15"


class WebviewRasp(Webview):
    def runJavaScript(self, javascript):
        self.page().currentFrame().evaluateJavaScript(javascript)

    def getUrl(self):
        return self.page().currentFrame().url().toString()


class WebviewDefault(Webview):