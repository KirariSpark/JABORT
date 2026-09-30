# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'appNeIehw.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QProgressBar,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QTabWidget, QVBoxLayout, QWidget)

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
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.ConvertorChildTab = QTabWidget(self.ConvertorLayout)
        self.ConvertorChildTab.setObjectName(u"ConvertorChildTab")
        self.ConvertorChildTab.setMovable(True)
        self.PNG2JPG = QWidget()
        self.PNG2JPG.setObjectName(u"PNG2JPG")
        self.verticalLayout = QVBoxLayout(self.PNG2JPG)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.PNG2JPGDir = QHBoxLayout()
        self.PNG2JPGDir.setObjectName(u"PNG2JPGDir")
        self.PNG2JPGFindDir = QPushButton(self.PNG2JPG)
        self.PNG2JPGFindDir.setObjectName(u"PNG2JPGFindDir")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PNG2JPGFindDir.sizePolicy().hasHeightForWidth())
        self.PNG2JPGFindDir.setSizePolicy(sizePolicy)

        self.PNG2JPGDir.addWidget(self.PNG2JPGFindDir)

        self.PNG2JPGDirTxt = QLineEdit(self.PNG2JPG)
        self.PNG2JPGDirTxt.setObjectName(u"PNG2JPGDirTxt")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.PNG2JPGDirTxt.sizePolicy().hasHeightForWidth())
        self.PNG2JPGDirTxt.setSizePolicy(sizePolicy1)
        self.PNG2JPGDirTxt.setClearButtonEnabled(True)

        self.PNG2JPGDir.addWidget(self.PNG2JPGDirTxt)


        self.verticalLayout.addLayout(self.PNG2JPGDir)

        self.PNG2JPGOptions = QGridLayout()
        self.PNG2JPGOptions.setObjectName(u"PNG2JPGOptions")
        self.PNG2JPGDelOri = QPushButton(self.PNG2JPG)
        self.PNG2JPGDelOri.setObjectName(u"PNG2JPGDelOri")
        self.PNG2JPGDelOri.setCheckable(True)

        self.PNG2JPGOptions.addWidget(self.PNG2JPGDelOri, 0, 0, 1, 1)

        self.PNG2JPGPreverveMeta = QPushButton(self.PNG2JPG)
        self.PNG2JPGPreverveMeta.setObjectName(u"PNG2JPGPreverveMeta")
        self.PNG2JPGPreverveMeta.setCheckable(True)

        self.PNG2JPGOptions.addWidget(self.PNG2JPGPreverveMeta, 0, 2, 1, 1)

        self.PNG2JPGSkipAlpha = QPushButton(self.PNG2JPG)
        self.PNG2JPGSkipAlpha.setObjectName(u"PNG2JPGSkipAlpha")
        self.PNG2JPGSkipAlpha.setCheckable(True)

        self.PNG2JPGOptions.addWidget(self.PNG2JPGSkipAlpha, 0, 1, 1, 1)

        self.PNG2JPGWalk = QPushButton(self.PNG2JPG)
        self.PNG2JPGWalk.setObjectName(u"PNG2JPGWalk")
        self.PNG2JPGWalk.setCheckable(True)

        self.PNG2JPGOptions.addWidget(self.PNG2JPGWalk, 1, 0, 1, 1)

        self.PNG2JPGDedup = QComboBox(self.PNG2JPG)
        self.PNG2JPGDedup.addItem("")
        self.PNG2JPGDedup.addItem("")
        self.PNG2JPGDedup.addItem("")
        self.PNG2JPGDedup.setObjectName(u"PNG2JPGDedup")

        self.PNG2JPGOptions.addWidget(self.PNG2JPGDedup, 1, 1, 1, 2)


        self.verticalLayout.addLayout(self.PNG2JPGOptions)

        self.PNG2JPGQuality = QHBoxLayout()
        self.PNG2JPGQuality.setObjectName(u"PNG2JPGQuality")
        self.PNG2JPGQualityTxt = QLabel(self.PNG2JPG)
        self.PNG2JPGQualityTxt.setObjectName(u"PNG2JPGQualityTxt")

        self.PNG2JPGQuality.addWidget(self.PNG2JPGQualityTxt)

        self.PNG2JPGQualitySlider = QSlider(self.PNG2JPG)
        self.PNG2JPGQualitySlider.setObjectName(u"PNG2JPGQualitySlider")
        self.PNG2JPGQualitySlider.setMinimum(1)
        self.PNG2JPGQualitySlider.setMaximum(100)
        self.PNG2JPGQualitySlider.setValue(80)
        self.PNG2JPGQualitySlider.setOrientation(Qt.Orientation.Horizontal)

        self.PNG2JPGQuality.addWidget(self.PNG2JPGQualitySlider)

        self.PNG2JPGQualityNum = QLabel(self.PNG2JPG)
        self.PNG2JPGQualityNum.setObjectName(u"PNG2JPGQualityNum")

        self.PNG2JPGQuality.addWidget(self.PNG2JPGQualityNum)


        self.verticalLayout.addLayout(self.PNG2JPGQuality)

        self.PNG2JPGProgress = QProgressBar(self.PNG2JPG)
        self.PNG2JPGProgress.setObjectName(u"PNG2JPGProgress")
        self.PNG2JPGProgress.setValue(0)
        self.PNG2JPGProgress.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.PNG2JPGProgress.setTextVisible(False)
        self.PNG2JPGProgress.setInvertedAppearance(False)

        self.verticalLayout.addWidget(self.PNG2JPGProgress)

        self.PNG2JPGBtns = QHBoxLayout()
        self.PNG2JPGBtns.setObjectName(u"PNG2JPGBtns")
        self.PNG2JPGRun = QPushButton(self.PNG2JPG)
        self.PNG2JPGRun.setObjectName(u"PNG2JPGRun")
        sizePolicy.setHeightForWidth(self.PNG2JPGRun.sizePolicy().hasHeightForWidth())
        self.PNG2JPGRun.setSizePolicy(sizePolicy)

        self.PNG2JPGBtns.addWidget(self.PNG2JPGRun)

        self.PNG2JPGStop = QPushButton(self.PNG2JPG)
        self.PNG2JPGStop.setObjectName(u"PNG2JPGStop")
        self.PNG2JPGStop.setEnabled(False)

        self.PNG2JPGBtns.addWidget(self.PNG2JPGStop)


        self.verticalLayout.addLayout(self.PNG2JPGBtns)

        self.PNG2JPGSpacer = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.PNG2JPGSpacer)

        self.ConvertorChildTab.addTab(self.PNG2JPG, "")
        self.Seq2PDF = QWidget()
        self.Seq2PDF.setObjectName(u"Seq2PDF")
        self.verticalLayout_18 = QVBoxLayout(self.Seq2PDF)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.Seq2PDFPath = QHBoxLayout()
        self.Seq2PDFPath.setObjectName(u"Seq2PDFPath")
        self.Seq2PDFPathOpen = QPushButton(self.Seq2PDF)
        self.Seq2PDFPathOpen.setObjectName(u"Seq2PDFPathOpen")

        self.Seq2PDFPath.addWidget(self.Seq2PDFPathOpen)

        self.Seq2PDFPathInput = QLineEdit(self.Seq2PDF)
        self.Seq2PDFPathInput.setObjectName(u"Seq2PDFPathInput")
        self.Seq2PDFPathInput.setClearButtonEnabled(True)

        self.Seq2PDFPath.addWidget(self.Seq2PDFPathInput)


        self.verticalLayout_18.addLayout(self.Seq2PDFPath)

        self.Seq2PDOptions = QHBoxLayout()
        self.Seq2PDOptions.setObjectName(u"Seq2PDOptions")
        self.Seq2PDFDel = QPushButton(self.Seq2PDF)
        self.Seq2PDFDel.setObjectName(u"Seq2PDFDel")
        self.Seq2PDFDel.setCheckable(True)

        self.Seq2PDOptions.addWidget(self.Seq2PDFDel)

        self.Seq2PDFRecursive = QPushButton(self.Seq2PDF)
        self.Seq2PDFRecursive.setObjectName(u"Seq2PDFRecursive")
        self.Seq2PDFRecursive.setCheckable(True)

        self.Seq2PDOptions.addWidget(self.Seq2PDFRecursive)


        self.verticalLayout_18.addLayout(self.Seq2PDOptions)

        self.Seq2PDFProgress = QProgressBar(self.Seq2PDF)
        self.Seq2PDFProgress.setObjectName(u"Seq2PDFProgress")
        self.Seq2PDFProgress.setValue(0)
        self.Seq2PDFProgress.setTextVisible(False)

        self.verticalLayout_18.addWidget(self.Seq2PDFProgress)

        self.Seq2PDFBtns = QHBoxLayout()
        self.Seq2PDFBtns.setObjectName(u"Seq2PDFBtns")
        self.Seq2PDFRun = QPushButton(self.Seq2PDF)
        self.Seq2PDFRun.setObjectName(u"Seq2PDFRun")

        self.Seq2PDFBtns.addWidget(self.Seq2PDFRun)

        self.Seq2PDFStop = QPushButton(self.Seq2PDF)
        self.Seq2PDFStop.setObjectName(u"Seq2PDFStop")
        self.Seq2PDFStop.setEnabled(False)

        self.Seq2PDFBtns.addWidget(self.Seq2PDFStop)


        self.verticalLayout_18.addLayout(self.Seq2PDFBtns)

        self.Seq2PDFSpacer = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_18.addItem(self.Seq2PDFSpacer)

        self.ConvertorChildTab.addTab(self.Seq2PDF, "")

        self.verticalLayout_3.addWidget(self.ConvertorChildTab)

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
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.ThemeDropdown.sizePolicy().hasHeightForWidth())
        self.ThemeDropdown.setSizePolicy(sizePolicy2)

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
        self.ConvertorChildTab.setCurrentIndex(1)
        self.PNG2JPGDedup.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Toolbox", None))
        self.MainPage.setTabText(self.MainPage.indexOf(self.FileMgrLayout), QCoreApplication.translate("Form", u"\u6587\u4ef6\u7ba1\u7406", None))
        self.PNG2JPGFindDir.setText(QCoreApplication.translate("Form", u"\u6253\u5f00", None))
        self.PNG2JPGDirTxt.setPlaceholderText(QCoreApplication.translate("Form", u"\u4ece\u6b64\u5904\u5f00\u59cb\u67e5\u627e\u56fe\u50cf", None))
        self.PNG2JPGDelOri.setText(QCoreApplication.translate("Form", u"\u5220\u9664\u539f\u6587\u4ef6", None))
        self.PNG2JPGPreverveMeta.setText(QCoreApplication.translate("Form", u"\u4fdd\u7559\u5143\u6570\u636e", None))
        self.PNG2JPGSkipAlpha.setText(QCoreApplication.translate("Form", u"\u8df3\u8fc7\u900f\u660e\u56fe", None))
        self.PNG2JPGWalk.setText(QCoreApplication.translate("Form", u"\u9012\u5f52\u67e5\u627e", None))
        self.PNG2JPGDedup.setItemText(0, QCoreApplication.translate("Form", u"\u91cd\u590d\u7684\u6587\u4ef6\uff1a\u8986\u76d6", None))
        self.PNG2JPGDedup.setItemText(1, QCoreApplication.translate("Form", u"\u91cd\u590d\u7684\u6587\u4ef6\uff1a\u8df3\u8fc7", None))
        self.PNG2JPGDedup.setItemText(2, QCoreApplication.translate("Form", u"\u91cd\u590d\u7684\u6587\u4ef6\uff1a\u589e\u52a0\u5e8f\u53f7", None))

        self.PNG2JPGDedup.setPlaceholderText(QCoreApplication.translate("Form", u"\u91cd\u590d\u7684\u6587\u4ef6", None))
        self.PNG2JPGQualityTxt.setText(QCoreApplication.translate("Form", u"\u8d28\u91cf", None))
        self.PNG2JPGQualityNum.setText(QCoreApplication.translate("Form", u"80", None))
        self.PNG2JPGProgress.setFormat(QCoreApplication.translate("Form", u"%p %", None))
        self.PNG2JPGRun.setText(QCoreApplication.translate("Form", u"\u8fd0\u884c", None))
        self.PNG2JPGStop.setText(QCoreApplication.translate("Form", u"\u7ec8\u6b62", None))
        self.ConvertorChildTab.setTabText(self.ConvertorChildTab.indexOf(self.PNG2JPG), QCoreApplication.translate("Form", u"PNG \u8f6c JPG", None))
#if QT_CONFIG(tooltip)
        self.ConvertorChildTab.setTabToolTip(self.ConvertorChildTab.indexOf(self.PNG2JPG), QCoreApplication.translate("Form", u"\u6279\u91cf\u7684\u5c06 PNG \u56fe\u50cf\u8f6c\u6362\u4e3a JPG \u56fe\u50cf", None))
#endif // QT_CONFIG(tooltip)
        self.Seq2PDFPathOpen.setText(QCoreApplication.translate("Form", u"\u6253\u5f00", None))
        self.Seq2PDFPathInput.setPlaceholderText(QCoreApplication.translate("Form", u"\u4ece\u6b64\u5904\u5f00\u59cb\u67e5\u627e\u56fe\u50cf", None))
        self.Seq2PDFDel.setText(QCoreApplication.translate("Form", u"\u5220\u9664\u539f\u6587\u4ef6", None))
        self.Seq2PDFRecursive.setText(QCoreApplication.translate("Form", u"\u9012\u5f52\u67e5\u627e", None))
        self.Seq2PDFRun.setText(QCoreApplication.translate("Form", u"\u8fd0\u884c", None))
        self.Seq2PDFStop.setText(QCoreApplication.translate("Form", u"\u7ec8\u6b62", None))
        self.ConvertorChildTab.setTabText(self.ConvertorChildTab.indexOf(self.Seq2PDF), QCoreApplication.translate("Form", u"\u56fe\u50cf\u5e8f\u5217\u8f6c PDF", None))
#if QT_CONFIG(tooltip)
        self.ConvertorChildTab.setTabToolTip(self.ConvertorChildTab.indexOf(self.Seq2PDF), QCoreApplication.translate("Form", u"\u5c06\u4e00\u4e2a\u6587\u4ef6\u5939\u4e2d\u7684\u56fe\u50cf\u5e8f\u5217\u8f6c\u6362\u4e3a\u5355\u4e2a PDF \u6587\u4ef6\uff0c\u4ee5\u7236\u6587\u4ef6\u5939\u547d\u540d\uff0c\u4fdd\u5b58\u5728\u56fe\u50cf\u5e8f\u5217\u6240\u5728\u7684\u4e0a\u4e00\u7ea7\u6587\u4ef6\u5939", None))
#endif // QT_CONFIG(tooltip)
        self.MainPage.setTabText(self.MainPage.indexOf(self.ConvertorLayout), QCoreApplication.translate("Form", u"\u8f6c\u6362\u5de5\u5177", None))
        self.MainPage.setTabText(self.MainPage.indexOf(self.MediaProcessingLayout), QCoreApplication.translate("Form", u"\u5a92\u4f53\u5904\u7406", None))
        self.MainPage.setTabText(self.MainPage.indexOf(self.TextProcessingLayout), QCoreApplication.translate("Form", u"\u6587\u672c\u5904\u7406", None))
        self.MainPage.setTabText(self.MainPage.indexOf(self.TestingLayout), QCoreApplication.translate("Form", u"\u6d4b\u8bd5\u7528", None))
        self.ThemeLabel.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u4e3b\u9898\uff08\u4e3b\u9898\u8def\u5f84\uff1a./Style\uff09", None))
        self.ThemeConfirm.setText(QCoreApplication.translate("Form", u"\u786e\u5b9a", None))
        self.ClearLog.setText(QCoreApplication.translate("Form", u"\u6e05\u9664\u65e5\u5fd7", None))
        self.MainPage.setTabText(self.MainPage.indexOf(self.SettingLayout), QCoreApplication.translate("Form", u"\u8bbe\u7f6e", None))
    # retranslateUi

