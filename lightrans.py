import re
import time
from threading import Thread, Lock

import keyboard
import pyperclip
from PySide6 import QtCore, QtGui
from PySide6.QtCore import QEvent, Qt
from PySide6.QtCore import Signal, QObject, QThread
from PySide6.QtGui import QTextCursor, QIcon
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QSystemTrayIcon, QMenu
from PySide6.QtWidgets import QMessageBox
from pynput import mouse

import resource_py.images
from account import Account
from capture import CaptureWidget
from resource_py.Baidu_ocr_API import baiduocrAPI
from resource_py.ErrorRecoder import errorrecoder
from resource_py.ecdict_API import ecdict_search
from resource_py.fanyi_text_api import fanyi_text
from resource_py.qss import lightqss
from resource_py.recorder import Recorder
from resource_py.stardict import StarDict
from resource_py.utils import resource_path, config_dir, open_folder_in_explorer

app_name="lightrans v1.8.6"

copytranslate_lock=Lock()
textbrowser_lock=Lock()

recorder=Recorder()
account=Account()

dict_path=resource_path('dict.db')
ecdict=StarDict(dict_path)

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
    return a
    # print(f'a={a}')


class MySignals(QObject):
    text_print = Signal(str)
    show_capture=Signal()
    translateSignal=Signal(str)

global_ms = MySignals()

langdic={"简体中文":"zh","Français":"fra","Español":"spa","English":"en","日本語":"jp","한국어 공부 해요":"kor","русский язык":"ru","繁體中文":"cht"}


class MainWindow(QObject): # 继承 QObject
    topping=1
    dict_mode=0
    auto_mode=0
    def __init__(self):
        super().__init__() # 调用父类构造函数
        self.ui=QUiLoader().load(resource_path("ui/lightrans.ui"))
        self.ui2=QUiLoader().load(resource_path("ui/setting.ui"))
        self.engine=None
        self.setengine(account.engine)
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

        # 创建系统托盘图标 (移除父窗口)
        self.tray_icon = QSystemTrayIcon()
        self.tray_icon.setIcon(QtGui.QIcon(':/eztrans256.ico'))
        self.tray_icon.setToolTip(app_name)

        # 创建托盘菜单
        tray_menu = QMenu()
        show_action = tray_menu.addAction("显示")
        show_action.triggered.connect(self.show_window)
        quit_action = tray_menu.addAction("退出")
        quit_action.triggered.connect(QApplication.instance().quit)
        self.tray_icon.setContextMenu(tray_menu)

        # 连接托盘图标激活信号
        self.tray_icon.activated.connect(self.tray_icon_activated)

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
        self.ui2.label_5.setText(f'{app_name}   项目主页: <a style="color:black" href="https://github.com/xunbu/lightrans">github主页</a>')
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
        self.ui2.buttonGroup.buttonClicked.connect(self.changeengine)
        self.ui2.pushButton_config.clicked.connect(self.open_config_dir)
        self.ui.widget_2.setVisible(False)

        self.ui2.comboBox_domain.currentIndexChanged.connect(self.changedomain)




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
        self.font.setFamily("Noto Sans CJK")
        # self.font.setFamily("微软雅黑")
        #调整词间距（只影响英文）
        self.font.setWordSpacing(0.3)
        #调整字间距
        self.font.setLetterSpacing(QtGui.QFont.PercentageSpacing,110)
        self.font.setPointSize(self.fontsize)
        self.ui.textEdit.setFont(self.font)
        cursor=self.setcursorindent()

        # 为主窗口安装事件过滤器
        self.ui.installEventFilter(self)

        self.changeengine()

        # 移除 changeEvent 方法
        # def changeEvent(self, event: QEvent):
    #     if event.type() == QEvent.Type.WindowStateChange:
    #         if self.windowState() & Qt.WindowState.WindowMinimized:
    #             # 窗口最小化时隐藏窗口并显示托盘图标
    #             self.tray_icon.show()
    #             self.hide() # 隐藏 MainWindow 自身
    #             event.ignore() # 阻止默认的最小化行为
    #             return
    #     super().changeEvent(event) # 调用基类实现

    # 托盘图标激活处理
    def tray_icon_activated(self, reason):
        if reason == QSystemTrayIcon.ActivationReason.Trigger: # 左键单击
            self.show_window()

    # 显示窗口
    def show_window(self):
        self.ui.showNormal() # 显示 self.ui
        self.ui.activateWindow() # 激活 self.ui
        self.tray_icon.hide()

    # 事件过滤器，用于处理窗口状态变化
    def eventFilter(self, watched, event):
        if watched == self.ui: # 检查事件是否来自主窗口
            if event.type() == QEvent.WindowStateChange:
                if self.ui.windowState() & Qt.WindowMinimized:
                    # 窗口最小化时隐藏窗口并显示托盘图标
                    self.tray_icon.show()
                    self.ui.hide()
                    return True # 事件已处理
            elif event.type() == QEvent.Close: # 检查关闭事件
                # 主窗口关闭时，也关闭设置窗口
                if hasattr(self, 'ui2') and self.ui2.isVisible():
                    self.ui2.close()
                # 不阻止主窗口的关闭事件，让它继续传递

        # 确保调用基类的 eventFilter
        return super(MainWindow, self).eventFilter(watched, event)

    def open_config_dir(self):
        open_folder_in_explorer(config_dir)

    def setcursorindent(self):
        self.ui.textEdit.clear()
        cursor=QTextCursor(self.ui.textEdit.document())
        block_format=cursor.blockFormat()
        block_format.setTextIndent(20)
        #调整行间距
        block_format.setLineHeight(130.0, 1)
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
        self.ui2.lineEdit_customAPI_url.setText(account.customAPI_url)
        self.ui2.lineEdit_customAPI_key.setText(account.customAPI_key)
        self.ui2.lineEdit_customAPI_model_id.setText(account.customAPI_model_id)
        self.ui2.lineEdit_zhipu_key.setText(account.zhipu_key)
        self.ui2.lineEdit_zhipu_model_id.setText(account.zhipu_model_id)
        self.ui2.lineEdit_baidu_id.setText(account.appid)
        self.ui2.lineEdit_baidu_key.setText(account.appkey)
        self.ui2.lineEdit_ocr_id.setText(account.client_id)
        self.ui2.lineEdit_ocr_key.setText(account.client_secret)
        self.ui2.lineEdit_select.setText(account.hotkey_select)
        self.ui2.lineEdit_input.setText(account.hotkey_input)
        self.ui2.lineEdit_screenshot.setText(account.hotkey_ocr)
        self.ui2.comboBox_domain.setEnabled(False)
        self.ui2.comboBox_domain.setCurrentIndex(['默认','生物医药','金融财经'].index(account.domain))
        self.ui2.show()

    #确认修改ID、key
    def changeidkey(self):
        keys_dict={}
        keys_dict["customAPI_url"]=self.ui2.lineEdit_customAPI_url.text()
        keys_dict["customAPI_key"]=self.ui2.lineEdit_customAPI_key.text()
        keys_dict["customAPI_model_id"]=self.ui2.lineEdit_customAPI_model_id.text()
        keys_dict["zhipu_key"]=self.ui2.lineEdit_zhipu_key.text()
        keys_dict["zhipu_model_id"]=self.ui2.lineEdit_zhipu_model_id.text()
        keys_dict["baidu_id"]=self.ui2.lineEdit_baidu_id.text()
        keys_dict["baidu_key"]=self.ui2.lineEdit_baidu_key.text()
        keys_dict["ocr_id"]=self.ui2.lineEdit_ocr_id.text()
        keys_dict["ocr_key"]=self.ui2.lineEdit_ocr_key.text()
        account.setidkey(keys_dict)
        self.ui2.lineEdit_customAPI_url.setText(account.customAPI_url)
        self.ui2.lineEdit_customAPI_key.setText(account.customAPI_key)
        self.ui2.lineEdit_customAPI_model_id.setText(account.customAPI_model_id)
        self.ui2.lineEdit_baidu_id.setText(account.appid)
        self.ui2.lineEdit_baidu_key.setText(account.appkey)
        self.ui2.lineEdit_ocr_id.setText(account.client_id)
        self.ui2.lineEdit_ocr_key.setText(account.client_secret)
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
    def setengine(self,engine:str):
        self.engine=engine
        self.ui2.engineSettingsStackedWidget.setVisible(True)
        if engine=='youdaozhiyun':
            self.ui2.engineSettingsStackedWidget.setVisible(False)
            self.ui2.radioButton_youdaozhiyun.setChecked(True)
        elif engine=='baidu':
            self.ui2.comboBox_domain.setEnabled(True)
            self.ui2.engineSettingsStackedWidget.setCurrentIndex(0)
            self.ui2.radioButton_baidu.setChecked(True)
        elif engine=='customAPI':
            self.ui2.engineSettingsStackedWidget.setCurrentIndex(1)
            self.ui2.radioButton_customAPI.setChecked(True)
        elif engine=='zhipu':
            self.engine ='zhipu'
            self.ui2.engineSettingsStackedWidget.setCurrentIndex(2)
            self.ui2.radioButton_zhipu.setChecked(True)
        account.setengine(engine)
        print(f"已写入{engine}")


    def changeengine(self):
        checkedbutton=self.ui2.buttonGroup.checkedButton()
        self.ui2.comboBox_domain.setEnabled(False)
        engine_dict={"有道智云":'youdaozhiyun',"百度翻译":"baidu","自定义":"customAPI","智谱":"zhipu"}
        for key in engine_dict:
            if key in checkedbutton.text():
                self.setengine(engine_dict[key])


    #修改垂直翻译
    def changedomain(self):
        domain = '默认'
        comboBox_domain=self.ui2.comboBox_domain
        if "默认" in comboBox_domain.currentText():
            pass
        elif "生物医药" in comboBox_domain.currentText():
            domain= '生物医药'
        elif "金融财经" in comboBox_domain.currentText():
            domain= '金融财经'
        account.setdomain(domain)

    def copytext(self):
        pyperclip.copy(self.ui.textEdit.toPlainText())
    def cleartext(self):
        print('清空')
        self.setcursorindent()

    def toppingwindow(self):
        if self.topping==0:
            # self.ui.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
            self.ui.windowHandle().setFlags(self.ui.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
            self.ui.pushButton_topping.setIcon(QIcon(r":/toppingblue.png"))
            self.topping=1
        else:
            # self.ui.setWindowFlags(QtCore.Qt.Widget)
            self.ui.windowHandle().setFlags(self.ui.windowFlags() & ~QtCore.Qt.WindowStaysOnTopHint)

            # self.ui.windowHandle().setFlags(QtCore.Qt.Widget)
            self.ui.pushButton_topping.setIcon(QIcon(r":/toppingblack.png"))
            self.topping=0
        # self.ui.show()

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
        # 显示正在翻译中
        textbrowser_lock.acquire()
        global_ms.text_print.emit('正在翻译中...')
        textbrowser_lock.release()

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
            if self.ui.checkBox_2.isChecked() or self.ui.checkBox_4.isChecked():  # 如果打开PDF模式或无换行复制
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
            if self.ui.checkBox_4.isChecked():
                print("123",self.ui.checkBox_4.isChecked())
                pyperclip.copy(str1)
                display = '已复制无换行文本到剪切板'
            else:
                if len(str1) != 0:
                    # 使用线程来执行翻译任务，避免界面卡死
                    def translate_thread():
                        result = fanyi_text(str1, engine=self.engine, to_lang=langdic[self.ui.comboBox.currentText()],domain=account.domain)
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
                        if self.ui.checkBox_3.isChecked() and not self.ui.checkBox_4.isChecked() and haveresult:
                            pyperclip.copy(display)
                        recorder.addrecord(display)
                        textbrowser_lock.acquire()
                        global_ms.text_print.emit(display)
                        textbrowser_lock.release()

                    thread = Thread(target=translate_thread)
                    thread.daemon = True
                    thread.start()
                    return
                else:
                    print('字符串为空，不进行翻译')
                    result = {"trans_result": [{'src': '', 'dst': ''}]}
                    display = ''

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
        thread1.daemon=True
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
        thread2.daemon=True
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
        thread3.daemon=True
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
            if self.ui.checkBox_3.isChecked() and haveresult:
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




#  pyinstaller -F --noconsole --icon="eztrans256.ico" --add-data="ui;ui" lightrans.py