# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settingDqaaFL.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QButtonGroup, QCheckBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form2(QWidget):
    def setupUi(self, Form2):
        if not Form2.objectName():
            Form2.setObjectName(u"Form2")
        Form2.resize(355, 422)
        self.verticalLayout_4 = QVBoxLayout(Form2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(Form2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setTextFormat(Qt.RichText)
        self.label_5.setOpenExternalLinks(True)
        self.label_5.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.verticalLayout_4.addWidget(self.label_5)

        self.checkBox = QCheckBox(Form2)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout_4.addWidget(self.checkBox)

        self.verticalSpacer_2 = QSpacerItem(20, 3, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 3, -1, -1)
        self.label_11 = QLabel(Form2)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_3.addWidget(self.label_11)

        self.radioButton_youdaozhiyun = QRadioButton(Form2)
        self.buttonGroup = QButtonGroup(Form2)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.radioButton_youdaozhiyun)
        self.radioButton_youdaozhiyun.setObjectName(u"radioButton_youdaozhiyun")
        self.radioButton_youdaozhiyun.setChecked(True)

        self.verticalLayout_3.addWidget(self.radioButton_youdaozhiyun)

        self.radioButton_youdao = QRadioButton(Form2)
        self.buttonGroup.addButton(self.radioButton_youdao)
        self.radioButton_youdao.setObjectName(u"radioButton_youdao")
        self.radioButton_youdao.setChecked(False)

        self.verticalLayout_3.addWidget(self.radioButton_youdao)

        self.radioButton_baiduReptile = QRadioButton(Form2)
        self.buttonGroup.addButton(self.radioButton_baiduReptile)
        self.radioButton_baiduReptile.setObjectName(u"radioButton_baiduReptile")

        self.verticalLayout_3.addWidget(self.radioButton_baiduReptile)

        self.radioButton_baidu = QRadioButton(Form2)
        self.buttonGroup.addButton(self.radioButton_baidu)
        self.radioButton_baidu.setObjectName(u"radioButton_baidu")

        self.verticalLayout_3.addWidget(self.radioButton_baidu)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 3, -1, -1)
        self.label_10 = QLabel(Form2)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout.addWidget(self.label_10)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_6 = QLabel(Form2)
        self.label_6.setObjectName(u"label_6")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_7.addWidget(self.label_6)

        self.lineEdit = QLineEdit(Form2)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy1)
        self.lineEdit.setMinimumSize(QSize(185, 0))

        self.horizontalLayout_7.addWidget(self.lineEdit)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_7 = QLabel(Form2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_6.addWidget(self.label_7)

        self.lineEdit_2 = QLineEdit(Form2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy1.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy1)
        self.lineEdit_2.setMinimumSize(QSize(185, 0))

        self.horizontalLayout_6.addWidget(self.lineEdit_2)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_8 = QLabel(Form2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_5.addWidget(self.label_8)

        self.lineEdit_3 = QLineEdit(Form2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        sizePolicy1.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy1)
        self.lineEdit_3.setMinimumSize(QSize(185, 0))

        self.horizontalLayout_5.addWidget(self.lineEdit_3)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_9 = QLabel(Form2)
        self.label_9.setObjectName(u"label_9")
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_4.addWidget(self.label_9)

        self.lineEdit_4 = QLineEdit(Form2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        sizePolicy1.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy1)
        self.lineEdit_4.setMinimumSize(QSize(185, 0))

        self.horizontalLayout_4.addWidget(self.lineEdit_4)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)

        self.pushButton_3 = QPushButton(Form2)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_4.addWidget(self.pushButton_3)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 3, -1, -1)
        self.label = QLabel(Form2)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(Form2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(50, 0))

        self.horizontalLayout.addWidget(self.label_2)

        self.lineEdit_select = QLineEdit(Form2)
        self.lineEdit_select.setObjectName(u"lineEdit_select")
        sizePolicy1.setHeightForWidth(self.lineEdit_select.sizePolicy().hasHeightForWidth())
        self.lineEdit_select.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.lineEdit_select)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(Form2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_2.addWidget(self.label_3)

        self.lineEdit_input = QLineEdit(Form2)
        self.lineEdit_input.setObjectName(u"lineEdit_input")
        sizePolicy1.setHeightForWidth(self.lineEdit_input.sizePolicy().hasHeightForWidth())
        self.lineEdit_input.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.lineEdit_input)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.pushButton = QPushButton(Form2)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(Form2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_3.addWidget(self.label_4)

        self.lineEdit_screenshot = QLineEdit(Form2)
        self.lineEdit_screenshot.setObjectName(u"lineEdit_screenshot")
        sizePolicy1.setHeightForWidth(self.lineEdit_screenshot.sizePolicy().hasHeightForWidth())
        self.lineEdit_screenshot.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.lineEdit_screenshot)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.pushButton_2 = QPushButton(Form2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_3.addWidget(self.pushButton_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)


        self.retranslateUi(Form2)

        QMetaObject.connectSlotsByName(Form2)
    # setupUi

    def retranslateUi(self, Form2):
        Form2.setWindowTitle(QCoreApplication.translate("Form2", u"\u8bbe\u7f6e", None))
        self.label_5.setText("")
        self.checkBox.setText(QCoreApplication.translate("Form2", u"OCR\u5206\u884c\u8f93\u51fa(\u9002\u5408\u8bc6\u522b\u4ee3\u7801\u7b49)", None))
        self.label_11.setText(QCoreApplication.translate("Form2", u"\u7ffb\u8bd1\u5f15\u64ce", None))
        self.radioButton_youdaozhiyun.setText(QCoreApplication.translate("Form2", u"\u6709\u9053\u667a\u4e91\uff08\u63a8\u8350\u3001\u514d\u8d39\u3001\u4e0d\u80fd\u7ffb\u8bd1\u8d85\u957f\u6bb5\u843d\uff09", None))
        self.radioButton_youdao.setText(QCoreApplication.translate("Form2", u"\u6709\u9053\u7ffb\u8bd1\uff08\u514d\u8d39\u3001\u6548\u679c\u8f83\u5dee\u3001\u4e0d\u7a33\u5b9a\u3001\u4e0d\u80fd\u7ffb\u8bd1\u5927\u6bb5\u6587\u5b57\uff09", None))
        self.radioButton_baiduReptile.setText(QCoreApplication.translate("Form2", u"\u767e\u5ea6\u7ffb\u8bd1\uff08\u514d\u8d39\u3001\u65e0\u9700\u586b\u5199\u8d26\u53f7\uff0c\u4e0d\u7a33\u5b9a\uff09", None))
        self.radioButton_baidu.setText(QCoreApplication.translate("Form2", u"\u767e\u5ea6API\uff08\u63a8\u8350\u4f7f\u7528\uff0c\u514d\u8d39\uff0c\u9700\u8981\u586b\u5199APPid\u3001APPkey\uff09", None))
        self.label_10.setText(QCoreApplication.translate("Form2", u"\u8d26\u53f7\u8bbe\u7f6e\uff08\u6309\u9700\u586b\u5199\uff0c\u8be6\u89c1\u9879\u76ee\u4e3b\u9875\uff09", None))
        self.label_6.setText(QCoreApplication.translate("Form2", u"APPid", None))
        self.label_7.setText(QCoreApplication.translate("Form2", u"APPkey", None))
        self.label_8.setText(QCoreApplication.translate("Form2", u"OCRid", None))
        self.label_9.setText(QCoreApplication.translate("Form2", u"OCRkey", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form2", u"\u786e\u8ba4\u8bbe\u7f6e", None))
        self.label.setText(QCoreApplication.translate("Form2", u"\u70ed\u952e\u8bbe\u7f6e", None))
        self.label_2.setText(QCoreApplication.translate("Form2", u"\u5212\u8bcd\u7ffb\u8bd1", None))
        self.label_3.setText(QCoreApplication.translate("Form2", u"\u8f93\u5165\u7ffb\u8bd1", None))
        self.pushButton.setText(QCoreApplication.translate("Form2", u"\u786e\u8ba4\u70ed\u952e", None))
        self.label_4.setText(QCoreApplication.translate("Form2", u"\u622a\u56fe\u70ed\u952e", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form2", u"\u6062\u590d\u9ed8\u8ba4\u8bbe\u7f6e", None))
    # retranslateUi

