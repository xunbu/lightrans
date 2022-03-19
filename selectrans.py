from ui1 import Ui_Form
from PySide6.QtWidgets import QApplication,QWidget
import time
from Baidu_Text_transAPI import baidu_trans
import json,re
import keyboard
import pyperclip
import images
from threading import Thread,Lock
from PySide6.QtCore import Signal ,QObject
from PySide6 import QtCore,QtGui


textbrowser_lock=Lock()

class MySignals(QObject):
    text_print = Signal(str)

global_ms = MySignals()

langdic={"简体中文":"zh","粤语":"yue","English":"en","日本語":"jp","한국어 공부 해요":"kor","русский язык":"ru","繁體中文":"cht"}

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        # 使用ui文件导入定义界面类
        self.ui = Ui_Form()
        # 初始化界面
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(':/eztrans256.ico'))
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint) # 窗体总在最前端
        self.ui.textBrowser.setPlaceholderText(r"版本V1.0.1 github地址：https://github.com/xunbu/selectrans" + '\n选中要翻译的内容,ctrl+c翻译\n输入要翻译的内容,ctrl+enter翻译\nctrl+c使用无换行复制')
        self.ui.checkBox.clicked.connect(self.toppingwindow)
        self.ui.pushButton.clicked.connect(self.increase_fontsize)
        self.ui.pushButton_2.clicked.connect(self.decrease_fontsize)

        self.delimitation_translation()
        self.translate()
        global_ms.text_print.connect(self.changdisplay)

        self.fontsize=12
        self.font=self.ui.textBrowser.font()
        self.font.setPointSize(self.fontsize)
        self.ui.textBrowser.setFont(self.font)


    def toppingwindow(self):
        if self.ui.checkBox.checkState():
            self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        else:
            self.setWindowFlags(QtCore.Qt.Widget)
        self.show()

    def increase_fontsize(self):
        self.fontsize+=1
        self.font.setPointSize(self.fontsize)
        self.ui.textBrowser.setFont(self.font)
        self.ui.textBrowser.setText(str(self.ui.textBrowser.toPlainText()))

    def decrease_fontsize(self):
        self.fontsize-=1
        self.font.setPointSize(self.fontsize)
        self.ui.textBrowser.setFont(self.font)
        self.ui.textBrowser.setText(str(self.ui.textBrowser.toPlainText()))

    def delimitation_translation(self):
        def run():
            print('子线程1开始')
            while 1:
                keyboard.wait('ctrl+c')  # 翻译触发按键
                keyboard.press_and_release('ctrl+c')
                time.sleep(0.1)
                str = pyperclip.paste()
                if self.ui.checkBox_2.checkState() or self.ui.checkBox_4.checkState():  # 如果打开PDF模式或无换行复制
                    list1 = [i for i in str]
                    # 将\r转为\r\n
                    for idx, i in enumerate(list1):
                        if idx == len(list1) - 1:
                            continue
                        if i == '\r' and list1[idx + 1] == '\n':
                            list1[idx] = '\r\n'
                            list1.pop(idx + 1)
                    for idx, i in enumerate(list1):
                        if idx == len(list1) - 1:
                            continue
                        if (i == '\r\n' or i == '\n' or i == '\r') and (
                                not (re.match("[a-zA-Z]", list1[idx - 1]) or re.match("[a-zA-Z]", list1[idx + 1]))) and \
                                list1[
                                    idx + 1] != ' ':
                            # 只有前后两个都是字母时才用空格分开
                            list1[idx] = ''
                        elif (i == '\r\n' or i == '\n' or i == '\r') and list1[idx + 1] != ' ':
                            list1[idx] = ' '
                    str = ''.join(list1)
                # 如果打开无换行复制，则不翻译
                if self.ui.checkBox_4.checkState():
                    pyperclip.copy(str)
                    display = '已复制无换行文本到剪切板'
                else:
                    if len(str) != 0:
                        result = json.loads(baidu_trans(str, to_lang=langdic[self.ui.comboBox.currentText()]))
                    else:
                        result = {"trans_result": [{'src': ' ', 'dst': ' '}]}
                    display = ''
                    for i in result['trans_result']:
                        display += '  ' + i['dst'] + '\n'
                    display=display[:-1]#去掉最后一个回车
                # 如果打开复制结果，则将结果复制到剪贴板中
                if self.ui.checkBox_3.checkState() and not self.ui.checkBox_4.checkState():
                    pyperclip.copy(display)
                textbrowser_lock.acquire()
                global_ms.text_print.emit(display)
                textbrowser_lock.release()

        thread1 = Thread(target=run)
        thread1.setDaemon(True)
        thread1.start()

    def translate(self):
        def run():
            print('子线程2开始')
            while 1:
                keyboard.wait('ctrl+enter')  # 翻译触发按键
                raw_str = self.ui.textBrowser.toPlainText()
                if len(raw_str) != 0:
                    result = json.loads(baidu_trans(raw_str, to_lang=langdic[self.ui.comboBox.currentText()]))
                else:
                    result = {"trans_result": [{'src': ' ', 'dst': ' '}]}
                display = ''
                for i in result['trans_result']:
                    display += '  ' + i['dst'] + '\n'
                display = display[:-1]  # 去掉最后一个回车
                if self.ui.checkBox_3.checkState():
                    pyperclip.copy(display)
                textbrowser_lock.acquire()
                global_ms.text_print.emit(display)
                textbrowser_lock.release()

        thread2 = Thread(target=run)
        thread2.setDaemon(True)
        thread2.start()


    def changdisplay(self,text):
        if self.ui.comboBox.currentText() in ["简体中文","粤语","繁體中文","日本語"]:
            self.font.setLetterSpacing(QtGui.QFont.PercentageSpacing,108)
            self.ui.textBrowser.setFont(self.font)
        else:
            self.font.setLetterSpacing(QtGui.QFont.PercentageSpacing,100)
            self.ui.textBrowser.setFont(self.font)

        self.ui.textBrowser.setText(text)


app = QApplication([])
mainw = MainWindow()
mainw.show()
app.exec()




