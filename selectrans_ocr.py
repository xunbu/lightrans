from ui.ui1 import Ui_Form
from ui.ui2 import Ui_Form2
from account import Account
from resource_py.qss import qss
from capture import CaptureWidget
from PySide6.QtWidgets import QApplication,QWidget
import time
from Baidu_Text_transAPI import baidu_trans
from Baidu_ocr_API import baiduocrAPI
import json,re
from pynput import mouse
import keyboard
import pyperclip
from threading import Thread,Lock
from PySide6.QtCore import Signal,QObject
from PySide6 import QtCore,QtGui
from PySide6.QtWidgets import QMessageBox
from PySide6.QtGui import QTextCursor,QIcon
from resource_py import images

copytranslate_lock=Lock()
textbrowser_lock=Lock()


account=Account()

hotkey_select=account.hotkey_select
hotkey_input=account.hotkey_input
hotkey_ocr=account.hotkey_ocr

def clipboard_ocr(picture_bytes):
    # print(f'picturebytes={picture_bytes}\ntype={type(picture_bytes)}')
    try:
        a = baiduocrAPI(picture_bytes)
    except:
        a=-1
    # print(f'a={a}')

    if type(a)==int:
        return -1
    else:
        return a


class MySignals(QObject):
    text_print = Signal(str)
    show_capture=Signal()
    translateSignal=Signal(str)

global_ms = MySignals()

langdic={"简体中文":"zh","粤语":"yue","English":"en","日本語":"jp","한국어 공부 해요":"kor","русский язык":"ru","繁體中文":"cht"}


class MainWindow(QWidget):
    topping=1
    def __init__(self):
        super().__init__()
        # 使用ui文件导入定义界面类
        self.ui = Ui_Form()
        self.ui2= Ui_Form2()
        # 初始化界面
        self.ui.setupUi(self)
        self.ui2.setupUi(self.ui2)
        self.setWindowIcon(QtGui.QIcon(':/eztrans256.ico'))
        self.ui2.setWindowIcon(QtGui.QIcon(':/eztrans256.ico'))
        self.ui2.setStyleSheet(qss)
        self.ui.pushButton_topping.setIcon(QIcon(r":/toppingblue.png"))
        self.ui.pushButton_setting.setIcon(QIcon(r":/setting.png"))
        self.ui.pushButton_copy.setIcon(QIcon(r":/copy.png"))
        self.ui.pushButton_expand.setIcon(QIcon(r":/up.png"))
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint) # 窗体总在最前端
        self.ui.textEdit.setPlaceholderText(f"划词翻译:选中要翻译的内容,{hotkey_select}翻译\n输入翻译:输入要翻译的内容,{hotkey_input}翻译\n无换行复制:{hotkey_select}复制无换行符文本\nOCR文字识别:{hotkey_ocr}")
        self.ui2.label_5.setText('V1.4.4 github地址:<a href="https://github.com/xunbu/selectrans">https://github.com/xunbu/selectrans</a>')
        self.ui.pushButton_topping.clicked.connect(self.toppingwindow)
        self.ui.pushButton_copy.clicked.connect(self.copytext)
        self.ui.pushButton_setting.clicked.connect(self.showsetting)
        self.ui.pushButton_expand.clicked.connect(self.changewidgetvisible)
        self.ui2.pushButton.clicked.connect(self.changehotkey)
        self.ui2.pushButton_2.clicked.connect(self.resethotkey)

        deleteShortcut = QtGui.QShortcut(QtGui.QKeySequence(QObject.tr("ctrl+up")), self)
        deleteShortcut.activated.connect(self.increase_fontsize)
        deleteShortcut = QtGui.QShortcut(QtGui.QKeySequence(QObject.tr("ctrl+down")), self)
        deleteShortcut.activated.connect(self.decrease_fontsize)

        self.ui.checkBox_5.clicked.connect(self.autotrans)
        global_ms.translateSignal.connect(self.copytranslate)
        global_ms.text_print.connect(self.changdisplay)
        global_ms.show_capture.connect(self.capturestart)
        self.delimitation_translation()
        self.translate()
        self.auto_flag = 0#用于判断是否应该自动翻译
        self.flag_ocr=0#flag1用于判断是否在OCR截屏中状态
        self.ocr()


        self.fontsize=12
        self.font=self.ui.textEdit.font()
        self.font.setWordSpacing(0.3)
        self.font.setLetterSpacing(QtGui.QFont.PercentageSpacing,102)
        self.font.setPointSize(self.fontsize)
        self.ui.textEdit.setFont(self.font)
        cursor=self.setcursorindent()





    def setcursorindent(self):
        self.ui.textEdit.clear()
        cursor=QTextCursor(self.ui.textEdit.document())
        block_format=cursor.blockFormat()
        block_format.setTextIndent(20)
        cursor.setBlockFormat(block_format)
        return cursor

    def changewidgetvisible(self):
        if self.ui.widget.isVisible():
            self.ui.pushButton_expand.setIcon(QIcon(r":/down.png"))
            self.ui.widget.setVisible(False)
        else:
            self.ui.pushButton_expand.setIcon(QIcon(r":/up.png"))
            self.ui.widget.setVisible(True)


    def showsetting(self):
        self.ui2.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.ui2.lineEdit_select.setText(account.hotkey_select)
        self.ui2.lineEdit_input.setText(account.hotkey_input)
        self.ui2.lineEdit_screenshot.setText(account.hotkey_ocr)
        self.ui2.show()

    def changehotkey(self):
        if self.ui2.lineEdit_select.text()!='' and self.ui2.lineEdit_input.text()!=''and self.ui2.lineEdit_screenshot.text()!='':
            args=self.ui2.lineEdit_select.text(),self.ui2.lineEdit_input.text(),self.ui2.lineEdit_screenshot.text()
            account.sethotkey(args)
            self.ui2.lineEdit_select.setText(account.hotkey_select)
            self.ui2.lineEdit_input.setText(account.hotkey_input)
            self.ui2.lineEdit_screenshot.setText(account.hotkey_ocr)
            QMessageBox.information(self.ui2,'操作成功','热键设置将在下次启动程序时生效')

    def resethotkey(self):
        args = 'ctrl+c','ctrl+enter','ctrl+alt'
        account.sethotkey(args)
        self.ui2.lineEdit_select.setText(account.hotkey_select)
        self.ui2.lineEdit_input.setText(account.hotkey_input)
        self.ui2.lineEdit_screenshot.setText(account.hotkey_ocr)
        QMessageBox.information(self.ui2, '操作成功', '热键设置将在下次启动程序时生效')


    def copytext(self):
        pyperclip.copy(self.ui.textEdit.toPlainText())

    def toppingwindow(self):
        if self.topping==0:
            self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
            self.ui.pushButton_topping.setIcon(QIcon(r":/toppingblue.png"))
            self.topping=1
        else:
            self.setWindowFlags(QtCore.Qt.Widget)
            self.ui.pushButton_topping.setIcon(QIcon(r":/toppingblack.png"))
            self.topping=0
        self.show()

    def autotrans(self):
        self.auto_flag=1
        if self.ui.checkBox_5.isChecked():
            def on_click(x, y, button, pressed):
                if self.auto_flag:
                    if pressed:#表示按下
                        pass
                    else:
                        clip_before=pyperclip.paste()
                        keyboard.send('ctrl+c')
                        time.sleep(0.1)
                        clip_after=pyperclip.paste()
                        if clip_after != clip_before and clip_after!='':
                            global_ms.translateSignal.emit(clip_after)
                    # if not pressed:
                    #     print(4)
                    #     # Stop listener
                    #     return False
                else:
                    return False
            listener = mouse.Listener(on_click=on_click)
            listener.setDaemon(True)
            listener.start()
        else:
            self.auto_flag=0


    def increase_fontsize(self):

        self.fontsize+=1
        self.font.setPointSize(self.fontsize)
        self.ui.textEdit.setFont(self.font)

        toplaintext=self.ui.textEdit.toPlainText()
        cursor=self.setcursorindent()
        cursor.insertText(toplaintext)

    def decrease_fontsize(self):
        self.fontsize-=1
        self.font.setPointSize(self.fontsize)
        self.ui.textEdit.setFont(self.font)

        toplaintext=self.ui.textEdit.toPlainText()
        cursor=self.setcursorindent()
        cursor.insertText(toplaintext)

    def  copytranslate(self,str):
        print('copytranslate')
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
                print('字符串为空，不进行翻译')
                result = {"trans_result": [{'src': ' ', 'dst': ' '}]}
            display = ''
            haveresult = 1
            if 'trans_result' in result:
                for i in result['trans_result']:
                    display += i['dst'] + '\n'
                display = display[:-1]  # 去掉最后一个回车
            else:
                # 接口使用过于频繁会停止
                haveresult = 0
                display = '翻译接口被占用，请再次尝试'
            # 如果打开复制结果，则将结果复制到剪贴板中
        if self.ui.checkBox_3.checkState() and not self.ui.checkBox_4.checkState() and haveresult:
            pyperclip.copy(display)
        textbrowser_lock.acquire()
        global_ms.text_print.emit(display)
        textbrowser_lock.release()

    def delimitation_translation(self):
        def run():
            print('子线程1开始')
            while 1:
                keyboard.wait(hotkey_select)  # 翻译触发按键
                print('划词翻译1')
                keyboard.send('ctrl+c')
                time.sleep(0.1)
                str1 = pyperclip.paste()
                global_ms.translateSignal.emit(str1)


        thread1 = Thread(target=run)
        thread1.setDaemon(True)
        thread1.start()

    def translate(self):
        def run():
            print('子线程2开始')
            while 1:
                keyboard.wait(hotkey_input)  # 翻译触发按键
                raw_str = self.ui.textEdit.toPlainText()
                if len(raw_str) != 0:
                    result = json.loads(baidu_trans(raw_str, to_lang=langdic[self.ui.comboBox.currentText()]))
                else:
                    result = {"trans_result": [{'src': ' ', 'dst': ' '}]}
                display = ''
                haveresult=1
                if 'trans_result' in result:
                    for i in result['trans_result']:
                        display += i['dst'] + '\n'
                    display = display[:-1]  # 去掉最后一个回车
                else:
                    # 接口使用过于频繁会停止
                    haveresult = 0
                    display = '翻译接口被占用，请再次尝试'
                if self.ui.checkBox_3.checkState() and haveresult:
                    pyperclip.copy(display)
                textbrowser_lock.acquire()
                global_ms.text_print.emit(display)
                textbrowser_lock.release()

        thread2 = Thread(target=run)
        thread2.setDaemon(True)
        thread2.start()

    def ocr(self):
        def run():
            print('子线程3开始')
            while 1:
                keyboard.wait(hotkey_ocr)
                if self.isVisible():
                    self.setVisible(False)
                time.sleep(0.3)  # 不加延时太快的话可能来不及隐藏界面
                global_ms.show_capture.emit()

        thread3 = Thread(target=run)
        thread3.setDaemon(True)
        thread3.start()

    def capturestart(self):
        self._captureW = CaptureWidget()  # 捕获窗口截图时创建CaptureWidget并覆盖整个屏幕
        self._captureW.show()

        # 收到信号后打印结果，关闭截图界面
        self._captureW.close_capture_signal.connect(self.close_capture_widget)
        self._captureW.capture_finished.connect(self.ocrQimage)

    def ocrQimage(self,imagebytes):
        ocr_result=clipboard_ocr(imagebytes)
        print(f'clipboard_ocr={ocr_result}')
        str=''
        if not isinstance(ocr_result,int):
            if 'language' in ocr_result:
                list1=[]
                list2=[]
                paragraph_space='\n'

                if ocr_result['language']==0:
                    #表示英语
                    joinstr=' '
                else:
                    joinstr=''
                if self.ui.checkBox_2.isChecked():
                    paragraph_space = joinstr
                for word in ocr_result['words_result']:
                    list1.append(word['words'])
                if self.ui2.checkBox.isChecked():#如果选择OCR不按段处理
                    print('定位4')
                    str='\n'.join(list1)
                else:
                    paragraphs_result = ocr_result['paragraphs_result']
                    for paragraph in paragraphs_result:
                        list2.append(joinstr.join([list1[idx] for idx in paragraph['words_result_idx']]))
                        str=paragraph_space.join(list2)
                        print(str)
            else:
                print('定位1')
                textbrowser_lock.acquire()
                global_ms.text_print.emit('截图为空')
                textbrowser_lock.release()
                return -1
        else:
            print('定位2')
            textbrowser_lock.acquire()
            global_ms.text_print.emit('OCR功能出错，请再次尝试')
            textbrowser_lock.release()
            return -1
        print(f'定位3={str}')
        pyperclip.copy(str)
        if self.ui.radioButton.isChecked():
            display=str
        else:
            if len(str) != 0:
                result = json.loads(baidu_trans(str, to_lang=langdic[self.ui.comboBox.currentText()]))
            else:
                result = {"trans_result": [{'src': ' ', 'dst': ' '}]}
            display = ''
            haveresult=1
            if 'trans_result' in result:
                for i in result['trans_result']:
                    display += i['dst'] + '\n'
                display=display[:-1]#去掉最后一个回车
            else:
                #接口使用过于频繁会停止
                haveresult=0
                display='翻译接口被占用，请再次尝试'
            if self.ui.checkBox_3.checkState() and haveresult:
                pyperclip.copy(display)
        textbrowser_lock.acquire()
        global_ms.text_print.emit(display)
        textbrowser_lock.release()

    # 关闭截图界面
    def close_capture_widget(self):
        self._captureW.close()
        self.setVisible(True)



    def changdisplay(self,text):
        cursor=self.setcursorindent()
        cursor.insertText(text)






app = QApplication([])
mainw = MainWindow()
mainw.show()
mainw.setStyleSheet(qss)
exit_code=app.exec()




