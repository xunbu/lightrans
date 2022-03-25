# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settingftebNM.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Form2(QWidget):
    def setupUi(self, Form2):
        if not Form2.objectName():
            Form2.setObjectName(u"Form2")
        Form2.resize(351, 180)
        self.verticalLayout = QVBoxLayout(Form2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_5 = QLabel(Form2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setTextFormat(Qt.AutoText)
        self.label_5.setOpenExternalLinks(True)
        self.label_5.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.verticalLayout.addWidget(self.label_5)

        self.checkBox = QCheckBox(Form2)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout.addWidget(self.checkBox)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.label = QLabel(Form2)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(Form2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.lineEdit_select = QLineEdit(Form2)
        self.lineEdit_select.setObjectName(u"lineEdit_select")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_select.sizePolicy().hasHeightForWidth())
        self.lineEdit_select.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.lineEdit_select)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(Form2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.lineEdit_input = QLineEdit(Form2)
        self.lineEdit_input.setObjectName(u"lineEdit_input")
        sizePolicy.setHeightForWidth(self.lineEdit_input.sizePolicy().hasHeightForWidth())
        self.lineEdit_input.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.lineEdit_input)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.pushButton = QPushButton(Form2)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(Form2)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.lineEdit_screenshot = QLineEdit(Form2)
        self.lineEdit_screenshot.setObjectName(u"lineEdit_screenshot")
        sizePolicy.setHeightForWidth(self.lineEdit_screenshot.sizePolicy().hasHeightForWidth())
        self.lineEdit_screenshot.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.lineEdit_screenshot)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.pushButton_2 = QPushButton(Form2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_3.addWidget(self.pushButton_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(Form2)

        QMetaObject.connectSlotsByName(Form2)
    # setupUi

    def retranslateUi(self, Form2):
        Form2.setWindowTitle(QCoreApplication.translate("Form2", u"\u8bbe\u7f6e", None))
        self.label_5.setText(QCoreApplication.translate("Form2", u"V1.4.4     github\u5730\u5740:https://github.com/xunbu/selectrans", None))
        self.checkBox.setText(QCoreApplication.translate("Form2", u"OCR\u5206\u884c\u8f93\u51fa(\u9002\u5408\u8bc6\u522b\u4ee3\u7801\u7b49)", None))
        self.label.setText(QCoreApplication.translate("Form2", u"\u70ed\u952e\u8bbe\u7f6e", None))
        self.label_2.setText(QCoreApplication.translate("Form2", u"\u5212\u8bcd\u7ffb\u8bd1", None))
        self.label_3.setText(QCoreApplication.translate("Form2", u"\u8f93\u5165\u7ffb\u8bd1", None))
        self.pushButton.setText(QCoreApplication.translate("Form2", u"\u786e\u8ba4\u70ed\u952e", None))
        self.label_4.setText(QCoreApplication.translate("Form2", u"\u622a\u56fe\u70ed\u952e", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form2", u"\u6062\u590d\u9ed8\u8ba4\u8bbe\u7f6e", None))
    # retranslateUi

