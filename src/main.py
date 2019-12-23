import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap, QMovie, QCursor
from PyQt5.QtCore import Qt


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'e-pet'
        self.left = 100
        self.top = 100
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create widget
        label = QLabel(self)
        # pixmap = QPixmap('../pic/cheer.gif')
        # label.setPixmap(pixmap)
        self.gif = QMovie('../pic/cheers.gif')
        pixmap = self.gif.currentPixmap()
        self.gif.frameChanged.connect(self.onNextFrame)

        label.setMovie(self.gif)
        self.gif.start()
        self.resize(pixmap.width(), pixmap.height())
        self.setMask(pixmap.mask())

        # 设置窗体无边框
        self.setWindowFlags(Qt.FramelessWindowHint)

        # 设置窗口置顶
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

        # 设置背景透明
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.show()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    def onNextFrame(self):
        pixmap = self.gif.currentPixmap()
        # self.setPixmap(pixmap)
        self.setMask(pixmap.mask())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
