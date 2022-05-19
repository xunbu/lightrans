import threading


from resource_py.stardict import StarDict
from account import Account
from resource_py.qss import lightqss,darkqss
from capture import CaptureWidget
from PySide6.QtWidgets import QApplication,QWidget
import time
from resource_py.fanyi_text_api import fanyi_text
from resource_py.Baidu_ocr_API import baiduocrAPI
from resource_py.recorder import Recorder
from resource_py.ErrorRecoder import errorrecoder
import json,re
from pynput import mouse
import keyboard
import pyperclip
from resource_py import images
from threading import Thread,Lock
from PySide6.QtCore import Signal,QObject,QThread
from PySide6 import QtCore,QtGui
from PySide6.QtWidgets import QMessageBox
from PySide6.QtGui import QTextCursor,QIcon
from PySide6.QtUiTools import QUiLoader
from resource_py.ecdict_API import ecdict_search

copytranslate_lock=Lock()
textbrowser_lock=Lock()

recorder=Recorder()
account=Account()

path='./dict.db'
ecdict=StarDict(path)

hotkey_select=account.hotkey_select
hotkey_input=account.hotkey_input
hotkey_ocr=account.hotkey_ocr

capturethread=QThread()

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

langdic={"简体中文":"zh","Français":"fra","Español":"spa","English":"en","日本語":"jp","한국어 공부 해요":"kor","русский язык":"ru","繁體中文":"cht"}


class MainWindow():
    topping=1
    dict_mode=0
    auto_mode=0
    def __init__(self):
        self.ui=QUiLoader().load(r"./ui/lightrans.ui")
        self.ui2=QUiLoader().load(r"./ui/setting.ui")
        self.engine=account.engine
        #应用qss样式表
        self.ui.setStyleSheet(lightqss)
        #如果使用py代码导入界面
        # 使用ui文件导入定义界面类
        # self.ui = Ui_Form()
        # self.ui2= Ui_Form2()
        # # 初始化界面
        # self.ui.setupUi(self)
        # self.ui2.setupUi(self.ui2)

        self.ui2.setStyleSheet(lightqss)
        self.ui.setWindowIcon(QtGui.QIcon(':/eztrans256.ico'))
        self.ui2.setWindowIcon(QtGui.QIcon(':/eztrans256.ico'))
        self.ui.pushButton_topping.setIcon(QIcon(r":/toppingblue.png"))
        self.ui.pushButton_setting.setIcon(QIcon(r":/setting.png"))
        self.ui.pushButton_copy.setIcon(QIcon(r":/copy.png"))
        self.ui.pushButton_expand.setIcon(QIcon(r":/up.png"))
        self.ui.pushButton_dict.setIcon(QIcon(r":/dict_black.png"))
        self.ui.pushButton_auto.setIcon(QIcon(r":/auto_black.png"))
        self.ui.pushButton_clear.setIcon(QIcon(r":/clear.png"))
        self.ui.pushButton_screenshot.setIcon(QIcon(r":/screenshot.png"))
        self.ui.pushButton_pre.setIcon(QIcon(r":/pre.png"))
        self.ui.pushButton_next.setIcon(QIcon(r":/next.png"))
        self.ui.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint) # 窗体总在最前端
        self.ui.textEdit.setPlaceholderText(f"划词翻译:选中要翻译的内容,{hotkey_select}翻译\n输入翻译:输入要翻译的内容,{hotkey_input}翻译\n无换行复制:{hotkey_select}复制无换行符文本\nOCR文字识别:{hotkey_ocr}")
        self.ui2.label_5.setText('V1.7.7   项目主页: <a style="color:black" href="https://www.xunbu.cc/lightrans">xunbu.cc/lightrans</a>')
        self.ui.pushButton_topping.clicked.connect(self.toppingwindow)
        self.ui.pushButton_copy.clicked.connect(self.copytext)
        self.ui.pushButton_setting.clicked.connect(self.showsetting)
        self.ui.pushButton_expand.clicked.connect(self.changewidgetvisible)
        self.ui.pushButton_dict.clicked.connect(self.changedictmode)
        self.ui.comboBox_2.activated.connect(self.searchcandidateword)
        self.ui.pushButton_clear.clicked.connect(self.cleartext)
        self.ui.pushButton_screenshot.clicked.connect(self.ocr_button)
        self.ui.pushButton.clicked.connect(self.translate)
        self.ui.pushButton_pre.clicked.connect(self.record_pre)
        self.ui.pushButton_next.clicked.connect(self.record_next)
        self.ui2.pushButton.clicked.connect(self.changehotkey)
        self.ui2.pushButton_2.clicked.connect(self.resethotkey)
        self.ui2.pushButton_3.clicked.connect(self.changeidkey)
        self.ui2.buttonGroup.buttonClicked.connect(self.changeengin)
        self.ui.widget_2.setVisible(False)




        increaseShortcut = QtGui.QShortcut(QtGui.QKeySequence(QObject.tr("ctrl+up")), self.ui)
        increaseShortcut.activated.connect(self.increase_fontsize)
        decreaseShortcut = QtGui.QShortcut(QtGui.QKeySequence(QObject.tr("ctrl+down")), self.ui)
        decreaseShortcut.activated.connect(self.decrease_fontsize)
        deleteShortcut = QtGui.QShortcut(QtGui.QKeySequence(QObject.tr("ctrl+delete")), self.ui)
        deleteShortcut.activated.connect(self.cleartext)


        self.ui.pushButton_auto.clicked.connect(self.autotrans)
        global_ms.translateSignal.connect(self.copytranslate)
        global_ms.text_print.connect(self.changdisplay)
        global_ms.show_capture.connect(self.capturestart)
        self.delimitation_translation()
        self.translate_input()
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

    def changedictmode(self):
        if self.dict_mode==0:
            self.dict_mode=1
            self.ui.pushButton_dict.setIcon(QIcon(r":/dict_blue.png"))
            self.ui.widget_2.setVisible(True)
            self.ui.textEdit.textChanged.connect(self.changecandidateword)
        else:
            self.dict_mode=0
            self.ui.pushButton_dict.setIcon(QIcon(r":/dict_black.png"))
            self.ui.widget_2.setVisible(False)
            self.ui.textEdit.textChanged.disconnect(self.changecandidateword)

    def changecandidateword(self):#词典模式下更改候选词
        self.ui.comboBox_2.clear()
        word=self.ui.textEdit.toPlainText().split('\n')[0]
        try:
            idx=word.index('[')
            wordlist=[i[1] for i in ecdict.match(word[0:idx-2])]
            print(word[0:idx])
        except:
            wordlist = [i[1] for i in ecdict.match(word)]
        self.ui.comboBox_2.addItems(wordlist)

    def searchcandidateword(self):#点击候选词后查询候选词
        global_ms.translateSignal.emit(self.ui.comboBox_2.currentText())

    def changewidgetvisible(self):
        if self.ui.widget.isVisible():
            self.ui.pushButton_expand.setIcon(QIcon(r":/down.png"))
            self.ui.widget.setVisible(False)
            self.ui.pushButton_expand.setToolTip('展开')
        else:
            self.ui.pushButton_expand.setIcon(QIcon(r":/up.png"))
            self.ui.widget.setVisible(True)
            self.ui.pushButton_expand.setToolTip('收起')

    def showsetting(self):
        self.ui2.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.ui2.lineEdit.setText(account.appid)
        self.ui2.lineEdit_2.setText(account.appkey)
        self.ui2.lineEdit_3.setText(account.client_id)
        self.ui2.lineEdit_4.setText(account.client_secret)
        self.ui2.lineEdit_select.setText(account.hotkey_select)
        self.ui2.lineEdit_input.setText(account.hotkey_input)
        self.ui2.lineEdit_screenshot.setText(account.hotkey_ocr)
        if self.engine== 'youdao':
            self.ui2.radioButton_youdao.setChecked(True)
        elif self.engine== 'baidu':
            self.ui2.radioButton_baidu.setChecked(True)
        elif self.engine=='baiduReptile':
            self.ui2.radioButton_baiduReptile.setChecked(True)
        elif self.engine=='youdaozhiyun':
            self.ui2.radioButton_youdaozhiyun.setChecked(True)
        self.ui2.show()

    #确认修改ID、key
    def changeidkey(self):
        args = self.ui2.lineEdit.text(), self.ui2.lineEdit_2.text(), self.ui2.lineEdit_3.text(),self.ui2.lineEdit_4.text()
        account.setidkey(args)
        self.ui2.lineEdit.setText(account.appid)
        self.ui2.lineEdit_2.setText(account.appkey)
        self.ui2.lineEdit_3.setText(account.client_id)
        self.ui2.lineEdit_4.setText(account.client_secret)
        QMessageBox.information(self.ui2, '操作成功', '设置成功')
    #确认修改热键
    def changehotkey(self):
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

    #修改翻译引擎
    def changeengin(self):
        checkedbutton=self.ui2.buttonGroup.checkedButton()
        if "有道翻译" in checkedbutton.text():
            self.engine= 'youdao'
        elif "百度API" in checkedbutton.text():
            self.engine= 'baidu'
        elif "百度翻译" in checkedbutton.text():
            self.engine = 'baiduReptile'
        elif "有道智云" in checkedbutton.text():
            self.engine ='youdaozhiyun'
        account.setengine(self.engine)

    def copytext(self):
        pyperclip.copy(self.ui.textEdit.toPlainText())
    def cleartext(self):
        print('清空')
        self.setcursorindent()

    def toppingwindow(self):
        if self.topping==0:
            self.ui.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
            self.ui.pushButton_topping.setIcon(QIcon(r":/toppingblue.png"))
            self.topping=1
        else:
            self.ui.setWindowFlags(QtCore.Qt.Widget)
            self.ui.pushButton_topping.setIcon(QIcon(r":/toppingblack.png"))
            self.topping=0
        self.show()

    #显示上一个record内容
    def record_pre(self):
        textbrowser_lock.acquire()
        global_ms.text_print.emit(recorder.prerecord())
        textbrowser_lock.release()

    def record_next(self):
        textbrowser_lock.acquire()
        global_ms.text_print.emit(recorder.nextrecord())
        textbrowser_lock.release()

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

    def autotrans(self):
        if self.auto_mode==0:
            self.auto_mode=1
            self.ui.pushButton_auto.setIcon(QIcon(r":/auto_blue.png"))
            print('自动模式开')
        else:
            self.auto_mode=0
            self.ui.pushButton_auto.setIcon(QIcon(r":/auto_black.png"))
            print('自动模式关')
        if self.auto_mode==1:
            def on_click(x, y, button, pressed):
                if self.auto_mode==1:
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

    #翻译识别主要函数
    def copytranslate(self, str1:str):
        print('copytranslate')
        if self.dict_mode==1:
            str1=str1.strip()
            print(str1)
            query=ecdict_search(str1,'query')
            if 'error' in query:
                display=query['error']
            else:
                display=f"{query['word']}  [{query['phonetic']}]\n" \
                                  f"{query['exchange'].replace('d:','过去分词:').replace('p:','过去式:').replace('3:','第三人称单数:').replace('i:','现在分词:').replace('s:','复数形式:').replace('r:','比较级:').replace('t:','最高级:')}" \
                                  f"\n{query['translation']}\n{query['definition']}"
        else:
            if self.ui.checkBox_2.checkState() or self.ui.checkBox_4.checkState():  # 如果打开PDF模式或无换行复制
                list1 = [i for i in str1]
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
                str1 = ''.join(list1)
            # 如果打开无换行复制，则不翻译
            haveresult = 1
            if self.ui.checkBox_4.checkState():
                pyperclip.copy(str1)
                display = '已复制无换行文本到剪切板'
            else:
                if len(str1) != 0:
                    result = fanyi_text(str1, engine=self.engine, to_lang=langdic[self.ui.comboBox.currentText()])
                else:
                    print('字符串为空，不进行翻译')
                    result = {"trans_result": [{'src': '', 'dst': ''}]}
                display = ''
                if 'trans_result' in result:
                    for i in result['trans_result']:
                        display += i['dst'] + '\n'
                    display = display[:-1]  # 去掉最后一个回车
                else:
                    # 接口使用过于频繁会停止
                    haveresult = 0
                    display = '翻译功能出错'+'\n'+errorrecoder.print_error_clear()
                # 如果打开复制结果，则将结果复制到剪贴板中
            if self.ui.checkBox_3.checkState() and not self.ui.checkBox_4.checkState() and haveresult:
                pyperclip.copy(display)

        recorder.addrecord(display)
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
                print(str1)
                global_ms.translateSignal.emit(str1)


        thread1 = Thread(target=run)
        thread1.setDaemon(True)
        thread1.start()

    def translate(self):
        global_ms.translateSignal.emit(self.ui.textEdit.toPlainText())

    def translate_input(self):
        def run():
            print('子线程2开始')
            while 1:
                keyboard.wait(hotkey_input)  # 翻译触发按键
                raw_str = self.ui.textEdit.toPlainText()
                global_ms.translateSignal.emit(raw_str)
        thread2 = Thread(target=run)
        thread2.setDaemon(True)
        thread2.start()

    def ocr_button(self):
        if self.ui.isVisible():
            self.ui.setVisible(False)
        time.sleep(0.3)  # 不加延时太快的话可能来不及隐藏界面
        global_ms.show_capture.emit()

    def ocr(self):
        def run():
            print('子线程3开始')
            while 1:
                keyboard.wait(hotkey_ocr)
                if self.ui.isVisible():
                    self.ui.setVisible(False)
                time.sleep(0.3)  # 不加延时太快的话可能来不及隐藏界面
                global_ms.show_capture.emit()

        thread3 = Thread(target=run)
        thread3.setDaemon(True)
        thread3.start()



    def capturestart(self):
        self._captureW = CaptureWidget()  # 捕获窗口截图时创建CaptureWidget并覆盖整个屏幕
        self._captureW.moveToThread(capturethread)
        self._captureW.show()

        # 收到信号后打印结果，关闭截图界面
        # self._captureW.showapp_signal.connect(self.showapp)#应该多线程实现，未来改进
        self._captureW.close_capture_signal.connect(self.close_capture_widget)
        self._captureW.capture_finished.connect(self.ocrQimage)

    def showapp(self):
        self.ui.setVisible(True)


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
            global_ms.text_print.emit('OCR功能出错，请再次尝试'+'\n'+errorrecoder.print_error_clear())
            textbrowser_lock.release()
            return -1
        print(f'定位3={str}')
        pyperclip.copy(str)
        if self.ui.radioButton.isChecked():
            display=str
        else:
            if len(str) != 0:
                result = fanyi_text(str, engine=self.engine, to_lang=langdic[self.ui.comboBox.currentText()])
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
                display='翻译功能出错'+'\n'+errorrecoder.print_error_clear()
            if self.ui.checkBox_3.checkState() and haveresult:
                pyperclip.copy(display)
        recorder.addrecord(display)
        textbrowser_lock.acquire()
        global_ms.text_print.emit(display)
        textbrowser_lock.release()

    # 关闭截图界面
    def close_capture_widget(self):
        self._captureW.close()
        self.ui.setVisible(True)


    def changdisplay(self,text):

        cursor=self.setcursorindent()
        cursor.insertText(text)






app = QApplication([])
mainw = MainWindow()
mainw.ui.show()
app.exec()




