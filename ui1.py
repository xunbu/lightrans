# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'easytransbRFvAz.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QHBoxLayout,
    QLayout, QPushButton, QSizePolicy, QSpacerItem,
    QTextBrowser, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(316, 435)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.checkBox = QCheckBox(Form)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI"])
        self.checkBox.setFont(font)
        self.checkBox.setLayoutDirection(Qt.LeftToRight)
        self.checkBox.setChecked(True)
        self.checkBox.setAutoExclusive(False)
        self.checkBox.setTristate(False)

        self.horizontalLayout.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(Form)
        self.checkBox_2.setObjectName(u"checkBox_2")
        sizePolicy.setHeightForWidth(self.checkBox_2.sizePolicy().hasHeightForWidth())
        self.checkBox_2.setSizePolicy(sizePolicy)
        self.checkBox_2.setChecked(False)

        self.horizontalLayout.addWidget(self.checkBox_2)

        self.checkBox_3 = QCheckBox(Form)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.horizontalLayout.addWidget(self.checkBox_3)

        self.checkBox_4 = QCheckBox(Form)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.horizontalLayout.addWidget(self.checkBox_4)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QSize(30, 0))

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QSize(30, 0))

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.comboBox = QComboBox(Form)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_2.addWidget(self.comboBox)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.horizontalSpacer = QSpacerItem(13, 13, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.textBrowser = QTextBrowser(Form)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setReadOnly(False)

        self.verticalLayout_2.addWidget(self.textBrowser)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"easytrans", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"\u7f6e\u9876", None))
        self.checkBox_2.setText(QCoreApplication.translate("Form", u"pdf\u6a21\u5f0f", None))
        self.checkBox_3.setText(QCoreApplication.translate("Form", u"\u590d\u5236\u8bd1\u6587", None))
        self.checkBox_4.setText(QCoreApplication.translate("Form", u"\u65e0\u6362\u884c\u590d\u5236", None))
#if QT_CONFIG(tooltip)
        self.pushButton.setToolTip(QCoreApplication.translate("Form", u"\u5b57\u53f7\u589e\u5927", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u5b57\u53f7+", None))
#if QT_CONFIG(tooltip)
        self.pushButton_2.setToolTip(QCoreApplication.translate("Form", u"\u5b57\u53f7\u51cf\u5c0f", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u5b57\u53f7-", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"\u7b80\u4f53\u4e2d\u6587", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"English", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"\u65e5\u672c\u8a9e", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Form", u"\ud55c\uad6d\uc5b4 \uacf5\ubd80 \ud574\uc694", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Form", u"\u0440\u0443\u0441\u0441\u043a\u0438\u0439 \u044f\u0437\u044b\u043a", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("Form", u"\u7e41\u9ad4\u4e2d\u6587", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("Form", u"\u7ca4\u8bed", None))

#if QT_CONFIG(tooltip)
        self.comboBox.setToolTip(QCoreApplication.translate("Form", u"\u9009\u62e9\u8981\u7ffb\u8bd1\u4e3a\u4ec0\u4e48\u8bed\u8a00", None))
#endif // QT_CONFIG(tooltip)
        self.comboBox.setCurrentText(QCoreApplication.translate("Form", u"\u7b80\u4f53\u4e2d\u6587", None))
        self.comboBox.setPlaceholderText("")
    # retranslateUi

