# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'appYJgjdZ.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QVBoxLayout, QWidget)

from pages.converters.ui import ConverterWidget
from pages.file_mgr.ui import FileMgrWidget
from pages.media_proc.ui import MediaProcWidget
from pages.tests.ui import TestsWidget
from pages.text_proc.ui import TextProcWidget

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(666, 677)
        icon = QIcon()
        icon.addFile(u"Icons/SP_TitleBarMenuButton.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Form.setWindowIcon(icon)
        self.formLayout = QFormLayout(Form)
        self.formLayout.setObjectName(u"formLayout")
        self.MainPage = QTabWidget(Form)
        self.MainPage.setObjectName(u"MainPage")
        self.MainPage.setTabShape(QTabWidget.TabShape.Rounded)
        self.MainPage.setMovable(True)
        self.FileMgrLayout = QWidget()
        self.FileMgrLayout.setObjectName(u"FileMgrLayout")
        self.verticalLayout_2 = QVBoxLayout(self.FileMgrLayout)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.FileMgr = FileMgrWidget(self.FileMgrLayout)
        self.FileMgr.setObjectName(u"FileMgr")

        self.verticalLayout_2.addWidget(self.FileMgr)

        self.MainPage.addTab(self.FileMgrLayout, "")
        self.ConvertorLayout = QWidget()
        self.ConvertorLayout.setObjectName(u"ConvertorLayout")
        self.verticalLayout_3 = QVBoxLayout(self.ConvertorLayout)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.ConverterWidget = ConverterWidget(self.ConvertorLayout)
        self.ConverterWidget.setObjectName(u"ConverterWidget")

        self.verticalLayout_3.addWidget(self.ConverterWidget)

        self.MainPage.addTab(self.ConvertorLayout, "")
        self.MediaProcessingLayout = QWidget()
        self.MediaProcessingLayout.setObjectName(u"MediaProcessingLayout")
        self.verticalLayout_5 = QVBoxLayout(self.MediaProcessingLayout)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.MediaProc = MediaProcWidget(self.MediaProcessingLayout)
        self.MediaProc.setObjectName(u"MediaProc")

        self.verticalLayout_5.addWidget(self.MediaProc)

        self.MainPage.addTab(self.MediaProcessingLayout, "")
        self.TextProcessingLayout = QWidget()
        self.TextProcessingLayout.setObjectName(u"TextProcessingLayout")
        self.verticalLayout_11 = QVBoxLayout(self.TextProcessingLayout)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.TextProcWidget = TextProcWidget(self.TextProcessingLayout)
        self.TextProcWidget.setObjectName(u"TextProcWidget")

        self.verticalLayout_11.addWidget(self.TextProcWidget)

        self.MainPage.addTab(self.TextProcessingLayout, "")
        self.TestingLayout = QWidget()
        self.TestingLayout.setObjectName(u"TestingLayout")
        self.verticalLayout_9 = QVBoxLayout(self.TestingLayout)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.TestingWidget = TestsWidget(self.TestingLayout)
        self.TestingWidget.setObjectName(u"TestingWidget")

        self.verticalLayout_9.addWidget(self.TestingWidget)

        self.MainPage.addTab(self.TestingLayout, "")
        self.SettingLayout = QWidget()
        self.SettingLayout.setObjectName(u"SettingLayout")
        self.verticalLayout_8 = QVBoxLayout(self.SettingLayout)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.ThemeLabel = QLabel(self.SettingLayout)
        self.ThemeLabel.setObjectName(u"ThemeLabel")

        self.verticalLayout_8.addWidget(self.ThemeLabel)

        self.ThemeChoose = QHBoxLayout()
        self.ThemeChoose.setObjectName(u"ThemeChoose")
        self.ThemeDropdown = QComboBox(self.SettingLayout)
        self.ThemeDropdown.setObjectName(u"ThemeDropdown")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ThemeDropdown.sizePolicy().hasHeightForWidth())
        self.ThemeDropdown.setSizePolicy(sizePolicy)

        self.ThemeChoose.addWidget(self.ThemeDropdown)

        self.ThemeConfirm = QPushButton(self.SettingLayout)
        self.ThemeConfirm.setObjectName(u"ThemeConfirm")

        self.ThemeChoose.addWidget(self.ThemeConfirm)


        self.verticalLayout_8.addLayout(self.ThemeChoose)

        self.ClearLog = QPushButton(self.SettingLayout)
        self.ClearLog.setObjectName(u"ClearLog")

        self.verticalLayout_8.addWidget(self.ClearLog)

        self.SettingsSpacer = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.SettingsSpacer)

        self.MainPage.addTab(self.SettingLayout, "")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.SpanningRole, self.MainPage)


        self.retranslateUi(Form)

        self.MainPage.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Toolbox", None))
        self.MainPage.setTabText(self.MainPage.indexOf(self.FileMgrLayout), QCoreApplication.translate("Form", u"\u6587\u4ef6\u7ba1\u7406", None))
        self.MainPage.setTabText(self.MainPage.indexOf(self.ConvertorLayout), QCoreApplication.translate("Form", u"\u8f6c\u6362\u5de5\u5177", None))
        self.MainPage.setTabText(self.MainPage.indexOf(self.MediaProcessingLayout), QCoreApplication.translate("Form", u"\u5a92\u4f53\u5904\u7406", None))
        self.MainPage.setTabText(self.MainPage.indexOf(self.TextProcessingLayout), QCoreApplication.translate("Form", u"\u6587\u672c\u5904\u7406", None))
        self.MainPage.setTabText(self.MainPage.indexOf(self.TestingLayout), QCoreApplication.translate("Form", u"\u6d4b\u8bd5\u7528", None))
        self.ThemeLabel.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u4e3b\u9898\uff08\u4e3b\u9898\u8def\u5f84\uff1a./Style\uff09", None))
        self.ThemeConfirm.setText(QCoreApplication.translate("Form", u"\u786e\u5b9a", None))
        self.ClearLog.setText(QCoreApplication.translate("Form", u"\u6e05\u9664\u65e5\u5fd7", None))
        self.MainPage.setTabText(self.MainPage.indexOf(self.SettingLayout), QCoreApplication.translate("Form", u"\u8bbe\u7f6e", None))
    # retranslateUi

