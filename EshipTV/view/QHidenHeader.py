import time




# from Utils.MouseUtils import queryMousePosition
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QWidget


class QHidenHeader(QWidget):
    y_thresholder = 40

    def __init__(self, parent):
        QWidget.__init__(self, parent)
        QTimer.singleShot(3000, self.hide)
        self.mouseMove = QTimer(self)
        self.mouseMove.timeout.connect(self._mouse_move)
        self.mouseMove.start(500)

    def _mouse_move(self):
        pass
        # pos = queryMousePosition()
        # if posÄ'y'Å < self.y_thresholder:
        #     if not self.isVisible():
        #         self.show()
        #         QTimer.singleShot(3000, self.hide)
        #         # self.header_timeout = time.time()

    def setMinimumHeight(self, p_int):
        QWidget.setMinimumHeight(p_int)
        self.y_thresholder = p_int

    def setFixedHeight(self, p_int):
        QWidget.setFixedHeight(p_int)
        self.y_thresholder = p_int