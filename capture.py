import threading
import time

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import Signal, Qt, QPoint, QRect,QRectF,QBuffer,QIODevice
from PySide6.QtGui import QPalette, QBrush, QPainter, QPen, QColor
import sys,datetime



class CaptureWidget(QWidget):
    # 自定义信号
    capture_finished = Signal(bytes)  # 将结果传给主界面
    close_capture_signal = Signal()
    showapp_signal=Signal()#让原界面显示

    def __init__(self):
        super().__init__()
        t = threading.currentThread()
        self.setWindowTitle('Capturing')
        self.setWindowFlags(Qt.FramelessWindowHint  # 无边框
                            | Qt.WindowStaysOnTopHint  # 页面置于最顶层
                            | Qt.Dialog)  # dialog样式，无按钮
        self.setWindowState(Qt.WindowFullScreen)  # 全屏
        # 获取当前屏幕的图像
        self.screen = QApplication.primaryScreen().grabWindow(0)

        # 配置调色板，将当前屏幕的图像画在widget上
        palette = QPalette()
        palette.setBrush(self.backgroundRole(), QBrush(self.screen))
        self.setPalette(palette)
        self.setCursor(Qt.CrossCursor)  # 设置鼠标样式为十字
        self.start, self.end = QPoint(), QPoint()  # 初始化起始点和终点

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:  # esc键退出
            self.close_capture_signal.emit()  # 关闭窗口

        return super().keyPressEvent(event)

    def paintEvent(self, event):
        if self.start == self.end:
            return super().paintEvent(event)

        # 设置绘图方式
        painter = QPainter(self)
        painter.setPen(QPen(QColor(255, 0, 0), 3))  # 画笔颜色，粗细
        painter.drawRect(QRectF(self.start, self.end))

        return super().paintEvent(event)

    def mousePressEvent(self, event):
        self.start =event.position()
        self.end = event.position()

        self.update()
        return super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        self.end = event.position()
        self.update()
        return super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if self.start == self.end:
            return super().mouseReleaseEvent(event)

        x1, x2 = sorted((self.start.x(), self.end.x()))
        y1, y2 = sorted((self.start.y(), self.end.y()))
        screen = QApplication.primaryScreen()
        screenShot= screen.grabWindow(0,int(x1),int(y1),int(x2-x1),int(y2-y1))
        self.setVisible(False)
        self.showapp_signal.emit()
        buffer = QBuffer()
        buffer.open(QIODevice.ReadWrite)
        screenShot.save(buffer, 'PNG')

        self.capture_finished.emit(bytes(buffer.data()))




        # 处理完关闭当前widget
        print('截图结束')
        # self.close()
        self.close_capture_signal.emit()


def main():
    app = QApplication(sys.argv)
    w = CaptureWidget()
    w.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

