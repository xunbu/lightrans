# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'easytrans_ocrZjlwRR.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QHBoxLayout,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(325, 354)
        self.verticalLayout_4 = QVBoxLayout(Form)
        self.verticalLayout_4.setSpacing(1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 1, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_topping = QPushButton(Form)
        self.pushButton_topping.setObjectName(u"pushButton_topping")
        self.pushButton_topping.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_topping.sizePolicy().hasHeightForWidth())
        self.pushButton_topping.setSizePolicy(sizePolicy)
        self.pushButton_topping.setMaximumSize(QSize(25, 25))
        self.pushButton_topping.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.pushButton_topping)

        self.pushButton_screenshot = QPushButton(Form)
        self.pushButton_screenshot.setObjectName(u"pushButton_screenshot")
        self.pushButton_screenshot.setMaximumSize(QSize(25, 25))
        self.pushButton_screenshot.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.pushButton_screenshot)

        self.pushButton_copy = QPushButton(Form)
        self.pushButton_copy.setObjectName(u"pushButton_copy")
        self.pushButton_copy.setEnabled(True)
        sizePolicy.setHeightForWidth(self.pushButton_copy.sizePolicy().hasHeightForWidth())
        self.pushButton_copy.setSizePolicy(sizePolicy)
        self.pushButton_copy.setMaximumSize(QSize(25, 25))
        self.pushButton_copy.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.pushButton_copy)

        self.pushButton_clear = QPushButton(Form)
        self.pushButton_clear.setObjectName(u"pushButton_clear")
        self.pushButton_clear.setMaximumSize(QSize(25, 25))
        self.pushButton_clear.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.pushButton_clear)

        self.pushButton_auto = QPushButton(Form)
        self.pushButton_auto.setObjectName(u"pushButton_auto")
        self.pushButton_auto.setMaximumSize(QSize(25, 25))
        self.pushButton_auto.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.pushButton_auto)

        self.pushButton_dict = QPushButton(Form)
        self.pushButton_dict.setObjectName(u"pushButton_dict")
        self.pushButton_dict.setMaximumSize(QSize(25, 25))
        self.pushButton_dict.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.pushButton_dict)

        self.pushButton_setting = QPushButton(Form)
        self.pushButton_setting.setObjectName(u"pushButton_setting")
        sizePolicy.setHeightForWidth(self.pushButton_setting.sizePolicy().hasHeightForWidth())
        self.pushButton_setting.setSizePolicy(sizePolicy)
        self.pushButton_setting.setMaximumSize(QSize(25, 25))
        self.pushButton_setting.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.pushButton_setting)

        self.pushButton_expand = QPushButton(Form)
        self.pushButton_expand.setObjectName(u"pushButton_expand")
        sizePolicy.setHeightForWidth(self.pushButton_expand.sizePolicy().hasHeightForWidth())
        self.pushButton_expand.setSizePolicy(sizePolicy)
        self.pushButton_expand.setMaximumSize(QSize(25, 25))
        self.pushButton_expand.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.pushButton_expand)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.horizontalLayout_4 = QHBoxLayout(self.widget)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(3, 0, 3, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton_pre = QPushButton(self.widget)
        self.pushButton_pre.setObjectName(u"pushButton_pre")
        sizePolicy.setHeightForWidth(self.pushButton_pre.sizePolicy().hasHeightForWidth())
        self.pushButton_pre.setSizePolicy(sizePolicy)
        self.pushButton_pre.setMinimumSize(QSize(0, 0))
        self.pushButton_pre.setMaximumSize(QSize(30, 50))
        self.pushButton_pre.setIconSize(QSize(15, 7))

        self.verticalLayout_2.addWidget(self.pushButton_pre)

        self.pushButton_next = QPushButton(self.widget)
        self.pushButton_next.setObjectName(u"pushButton_next")
        sizePolicy.setHeightForWidth(self.pushButton_next.sizePolicy().hasHeightForWidth())
        self.pushButton_next.setSizePolicy(sizePolicy)
        self.pushButton_next.setMinimumSize(QSize(0, 0))
        self.pushButton_next.setMaximumSize(QSize(30, 50))
        self.pushButton_next.setIconSize(QSize(15, 7))

        self.verticalLayout_2.addWidget(self.pushButton_next)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.checkBox_2 = QCheckBox(self.widget)
        self.checkBox_2.setObjectName(u"checkBox_2")
        sizePolicy.setHeightForWidth(self.checkBox_2.sizePolicy().hasHeightForWidth())
        self.checkBox_2.setSizePolicy(sizePolicy)
        self.checkBox_2.setChecked(False)

        self.horizontalLayout_2.addWidget(self.checkBox_2)

        self.checkBox_3 = QCheckBox(self.widget)
        self.checkBox_3.setObjectName(u"checkBox_3")
        sizePolicy.setHeightForWidth(self.checkBox_3.sizePolicy().hasHeightForWidth())
        self.checkBox_3.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.checkBox_3)

        self.checkBox_4 = QCheckBox(self.widget)
        self.checkBox_4.setObjectName(u"checkBox_4")
        sizePolicy.setHeightForWidth(self.checkBox_4.sizePolicy().hasHeightForWidth())
        self.checkBox_4.setSizePolicy(sizePolicy)
        self.checkBox_4.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_2.addWidget(self.checkBox_4)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.radioButton = QRadioButton(self.widget)
        self.radioButton.setObjectName(u"radioButton")
        sizePolicy.setHeightForWidth(self.radioButton.sizePolicy().hasHeightForWidth())
        self.radioButton.setSizePolicy(sizePolicy)
        self.radioButton.setChecked(True)

        self.horizontalLayout_3.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.widget)
        self.radioButton_2.setObjectName(u"radioButton_2")
        sizePolicy.setHeightForWidth(self.radioButton_2.sizePolicy().hasHeightForWidth())
        self.radioButton_2.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.radioButton_2)

        self.comboBox = QComboBox(self.widget)
        self.comboBox.addItem("")
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
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.comboBox.setFrame(False)

        self.horizontalLayout_3.addWidget(self.comboBox)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_4.addLayout(self.verticalLayout)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        self.pushButton.setMinimumSize(QSize(30, 50))
        self.pushButton.setMaximumSize(QSize(30, 50))
        self.pushButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.pushButton)

        self.horizontalSpacer = QSpacerItem(4, 13, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)


        self.verticalLayout_4.addWidget(self.widget)

        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.comboBox_2 = QComboBox(self.widget_2)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout_5.addWidget(self.comboBox_2)


        self.verticalLayout_4.addWidget(self.widget_2)

        self.widget_3 = QWidget(Form)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_3 = QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(7, 0, 7, 7)
        self.textEdit = QTextEdit(self.widget_3)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy2)

        self.verticalLayout_3.addWidget(self.textEdit)


        self.verticalLayout_4.addWidget(self.widget_3)


        self.retranslateUi(Form)

        self.comboBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"lightrans", None))
#if QT_CONFIG(tooltip)
        self.pushButton_topping.setToolTip(QCoreApplication.translate("Form", u"\u7f6e\u9876", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_topping.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_screenshot.setToolTip(QCoreApplication.translate("Form", u"\u6587\u5b57\u8bc6\u522b", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_screenshot.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_copy.setToolTip(QCoreApplication.translate("Form", u"\u590d\u5236", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_copy.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_clear.setToolTip(QCoreApplication.translate("Form", u"\u6e05\u7a7a", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_clear.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_auto.setToolTip(QCoreApplication.translate("Form", u"\u81ea\u52a8\u6a21\u5f0f", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_auto.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_dict.setToolTip(QCoreApplication.translate("Form", u"\u8bcd\u5178\u6a21\u5f0f", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_dict.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_setting.setToolTip(QCoreApplication.translate("Form", u"\u8bbe\u7f6e", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_setting.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_expand.setToolTip(QCoreApplication.translate("Form", u"\u6536\u8d77", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_expand.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_pre.setToolTip(QCoreApplication.translate("Form", u"\u4e0a\u4e00\u4e2a", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_pre.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_next.setToolTip(QCoreApplication.translate("Form", u"\u4e0b\u4e00\u4e2a", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_next.setText("")
#if QT_CONFIG(tooltip)
        self.checkBox_2.setToolTip(QCoreApplication.translate("Form", u"\u53bb\u6389\u6587\u672c\u6362\u884c(\u9002\u7528\u4e8epdf/OCR\u7b49)", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_2.setText(QCoreApplication.translate("Form", u"\u53bb\u9664\u6362\u884c", None))
#if QT_CONFIG(tooltip)
        self.checkBox_3.setToolTip(QCoreApplication.translate("Form", u"\u52fe\u9009\u540e\u8bd1\u6587\u5c06\u81ea\u52a8\u590d\u5236\u5230\u526a\u8d34\u677f\u4e0a", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_3.setText(QCoreApplication.translate("Form", u"\u81ea\u52a8\u590d\u5236\u8bd1\u6587", None))
#if QT_CONFIG(tooltip)
        self.checkBox_4.setToolTip(QCoreApplication.translate("Form", u"\u5212\u8bcd\u7ffb\u8bd1\u5931\u6548", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_4.setText(QCoreApplication.translate("Form", u"\u65e0\u6362\u884c\u590d\u5236", None))
#if QT_CONFIG(tooltip)
        self.radioButton.setToolTip(QCoreApplication.translate("Form", u"\u8bc6\u522b\u7ed3\u679c\u5c06\u81ea\u52a8\u590d\u5236\u5230\u526a\u8d34\u677f", None))
#endif // QT_CONFIG(tooltip)
        self.radioButton.setText(QCoreApplication.translate("Form", u"OCR\u590d\u5236", None))
#if QT_CONFIG(tooltip)
        self.radioButton_2.setToolTip(QCoreApplication.translate("Form", u"\u5f00\u542f\u622a\u56fe\u7ffb\u8bd1", None))
#endif // QT_CONFIG(tooltip)
        self.radioButton_2.setText(QCoreApplication.translate("Form", u"OCR\u7ffb\u8bd1", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"\u7b80\u4f53\u4e2d\u6587", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"English", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"Fran\u00e7ais", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Form", u"\u65e5\u672c\u8a9e", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Form", u"\ud55c\uad6d\uc5b4 \uacf5\ubd80 \ud574\uc694", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("Form", u"\u0440\u0443\u0441\u0441\u043a\u0438\u0439 \u044f\u0437\u044b\u043a", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("Form", u"Espa\u00f1ol", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("Form", u"\u7e41\u9ad4\u4e2d\u6587", None))

#if QT_CONFIG(tooltip)
        self.comboBox.setToolTip(QCoreApplication.translate("Form", u"\u9009\u62e9\u8bd1\u6587\u8bed\u8a00", None))
#endif // QT_CONFIG(tooltip)
        self.comboBox.setCurrentText(QCoreApplication.translate("Form", u"\u7b80\u4f53\u4e2d\u6587", None))
        self.comboBox.setPlaceholderText("")
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u7ffb\u8bd1", None))
        self.textEdit.setPlaceholderText("")
    # retranslateUi

