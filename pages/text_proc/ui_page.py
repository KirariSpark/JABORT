# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pagexuASzK.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QHBoxLayout,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QTabWidget, QVBoxLayout, QWidget)

class Ui_TextProcWidget(object):
    def setupUi(self, TextProcWidget):
        if not TextProcWidget.objectName():
            TextProcWidget.setObjectName(u"TextProcWidget")
        TextProcWidget.resize(406, 394)
        self.horizontalLayout = QHBoxLayout(TextProcWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.TextProcChildTab = QTabWidget(TextProcWidget)
        self.TextProcChildTab.setObjectName(u"TextProcChildTab")
        self.TextProcChildTab.setMovable(True)
        self.CropText = QWidget()
        self.CropText.setObjectName(u"CropText")
        self.verticalLayout_6 = QVBoxLayout(self.CropText)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.CropTextInput = QHBoxLayout()
        self.CropTextInput.setObjectName(u"CropTextInput")
        self.CropTextInPathOpen = QPushButton(self.CropText)
        self.CropTextInPathOpen.setObjectName(u"CropTextInPathOpen")

        self.CropTextInput.addWidget(self.CropTextInPathOpen)

        self.CropTextInPath = QLineEdit(self.CropText)
        self.CropTextInPath.setObjectName(u"CropTextInPath")
        self.CropTextInPath.setClearButtonEnabled(True)

        self.CropTextInput.addWidget(self.CropTextInPath)


        self.verticalLayout_6.addLayout(self.CropTextInput)

        self.CropTextOptions = QHBoxLayout()
        self.CropTextOptions.setObjectName(u"CropTextOptions")
        self.CropTextRatioSpinbox = QSpinBox(self.CropText)
        self.CropTextRatioSpinbox.setObjectName(u"CropTextRatioSpinbox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CropTextRatioSpinbox.sizePolicy().hasHeightForWidth())
        self.CropTextRatioSpinbox.setSizePolicy(sizePolicy)
        self.CropTextRatioSpinbox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.CropTextRatioSpinbox.setMinimum(1)
        self.CropTextRatioSpinbox.setMaximum(100)

        self.CropTextOptions.addWidget(self.CropTextRatioSpinbox)

        self.CropTextDedup = QComboBox(self.CropText)
        self.CropTextDedup.addItem("")
        self.CropTextDedup.addItem("")
        self.CropTextDedup.addItem("")
        self.CropTextDedup.setObjectName(u"CropTextDedup")
        sizePolicy.setHeightForWidth(self.CropTextDedup.sizePolicy().hasHeightForWidth())
        self.CropTextDedup.setSizePolicy(sizePolicy)

        self.CropTextOptions.addWidget(self.CropTextDedup)


        self.verticalLayout_6.addLayout(self.CropTextOptions)

        self.CropTextOutput = QHBoxLayout()
        self.CropTextOutput.setObjectName(u"CropTextOutput")
        self.CropTextOutPathOpen = QPushButton(self.CropText)
        self.CropTextOutPathOpen.setObjectName(u"CropTextOutPathOpen")

        self.CropTextOutput.addWidget(self.CropTextOutPathOpen)

        self.CropTextOutPath = QLineEdit(self.CropText)
        self.CropTextOutPath.setObjectName(u"CropTextOutPath")
        self.CropTextOutPath.setClearButtonEnabled(True)

        self.CropTextOutput.addWidget(self.CropTextOutPath)


        self.verticalLayout_6.addLayout(self.CropTextOutput)

        self.CroptextRun = QPushButton(self.CropText)
        self.CroptextRun.setObjectName(u"CroptextRun")

        self.verticalLayout_6.addWidget(self.CroptextRun)

        self.CropTextSpacer = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.CropTextSpacer)

        self.TextProcChildTab.addTab(self.CropText, "")
        self.CalSim = QWidget()
        self.CalSim.setObjectName(u"CalSim")
        self.verticalLayout_14 = QVBoxLayout(self.CalSim)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.CalSimModel = QHBoxLayout()
        self.CalSimModel.setObjectName(u"CalSimModel")
        self.CalSimModelDropdown = QComboBox(self.CalSim)
        self.CalSimModelDropdown.setObjectName(u"CalSimModelDropdown")
        sizePolicy.setHeightForWidth(self.CalSimModelDropdown.sizePolicy().hasHeightForWidth())
        self.CalSimModelDropdown.setSizePolicy(sizePolicy)

        self.CalSimModel.addWidget(self.CalSimModelDropdown)

        self.CalSimModelRefresh = QPushButton(self.CalSim)
        self.CalSimModelRefresh.setObjectName(u"CalSimModelRefresh")

        self.CalSimModel.addWidget(self.CalSimModelRefresh)

        self.CalSimPersistentModel = QPushButton(self.CalSim)
        self.CalSimPersistentModel.setObjectName(u"CalSimPersistentModel")
        self.CalSimPersistentModel.setCheckable(True)

        self.CalSimModel.addWidget(self.CalSimPersistentModel)


        self.verticalLayout_14.addLayout(self.CalSimModel)

        self.CalSimInput = QHBoxLayout()
        self.CalSimInput.setObjectName(u"CalSimInput")
        self.CalSimIn1 = QLineEdit(self.CalSim)
        self.CalSimIn1.setObjectName(u"CalSimIn1")
        self.CalSimIn1.setClearButtonEnabled(True)

        self.CalSimInput.addWidget(self.CalSimIn1)

        self.CalSimIn2 = QLineEdit(self.CalSim)
        self.CalSimIn2.setObjectName(u"CalSimIn2")
        self.CalSimIn2.setClearButtonEnabled(True)

        self.CalSimInput.addWidget(self.CalSimIn2)


        self.verticalLayout_14.addLayout(self.CalSimInput)

        self.CalSimBtns = QHBoxLayout()
        self.CalSimBtns.setObjectName(u"CalSimBtns")
        self.CalSimRun = QPushButton(self.CalSim)
        self.CalSimRun.setObjectName(u"CalSimRun")

        self.CalSimBtns.addWidget(self.CalSimRun)

        self.CalSimUnload = QPushButton(self.CalSim)
        self.CalSimUnload.setObjectName(u"CalSimUnload")

        self.CalSimBtns.addWidget(self.CalSimUnload)


        self.verticalLayout_14.addLayout(self.CalSimBtns)

        self.CalSimSpacer = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_14.addItem(self.CalSimSpacer)

        self.TextProcChildTab.addTab(self.CalSim, "")
        self.JsonSorter = QWidget()
        self.JsonSorter.setObjectName(u"JsonSorter")
        self.verticalLayout_15 = QVBoxLayout(self.JsonSorter)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.JsonSorterIn = QHBoxLayout()
        self.JsonSorterIn.setObjectName(u"JsonSorterIn")
        self.JsonSorterInOpen = QPushButton(self.JsonSorter)
        self.JsonSorterInOpen.setObjectName(u"JsonSorterInOpen")

        self.JsonSorterIn.addWidget(self.JsonSorterInOpen)

        self.JsonSorterInPath = QLineEdit(self.JsonSorter)
        self.JsonSorterInPath.setObjectName(u"JsonSorterInPath")
        self.JsonSorterInPath.setClearButtonEnabled(True)

        self.JsonSorterIn.addWidget(self.JsonSorterInPath)


        self.verticalLayout_15.addLayout(self.JsonSorterIn)

        self.JsonSorterRun = QPushButton(self.JsonSorter)
        self.JsonSorterRun.setObjectName(u"JsonSorterRun")

        self.verticalLayout_15.addWidget(self.JsonSorterRun)

        self.JsonSorterSpacer = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_15.addItem(self.JsonSorterSpacer)

        self.TextProcChildTab.addTab(self.JsonSorter, "")

        self.horizontalLayout.addWidget(self.TextProcChildTab)


        self.retranslateUi(TextProcWidget)

        self.TextProcChildTab.setCurrentIndex(0)
        self.CropTextDedup.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(TextProcWidget)
    # setupUi

    def retranslateUi(self, TextProcWidget):
        TextProcWidget.setWindowTitle(QCoreApplication.translate("TextProcWidget", u"Form", None))
        self.CropTextInPathOpen.setText(QCoreApplication.translate("TextProcWidget", u"\u6253\u5f00", None))
        self.CropTextInPath.setPlaceholderText(QCoreApplication.translate("TextProcWidget", u"\u8f93\u5165\u6587\u4ef6\u8def\u5f84", None))
        self.CropTextRatioSpinbox.setSuffix(QCoreApplication.translate("TextProcWidget", u" %", None))
        self.CropTextRatioSpinbox.setPrefix(QCoreApplication.translate("TextProcWidget", u"\u622a\u53d6\u6587\u672c\u7684\u540e ", None))
        self.CropTextDedup.setItemText(0, QCoreApplication.translate("TextProcWidget", u"\u91cd\u590d\u7684\u6587\u4ef6\uff1a\u8986\u76d6", None))
        self.CropTextDedup.setItemText(1, QCoreApplication.translate("TextProcWidget", u"\u91cd\u590d\u7684\u6587\u4ef6\uff1a\u8df3\u8fc7", None))
        self.CropTextDedup.setItemText(2, QCoreApplication.translate("TextProcWidget", u"\u91cd\u590d\u7684\u6587\u4ef6\uff1a\u589e\u52a0\u5e8f\u53f7", None))

        self.CropTextDedup.setPlaceholderText(QCoreApplication.translate("TextProcWidget", u"\u91cd\u590d\u7684\u6587\u4ef6", None))
        self.CropTextOutPathOpen.setText(QCoreApplication.translate("TextProcWidget", u"\u6253\u5f00", None))
        self.CropTextOutPath.setPlaceholderText(QCoreApplication.translate("TextProcWidget", u"\u8f93\u51fa\u6587\u4ef6\u8def\u5f84\uff08\u7559\u7a7a\u4ee5\u4fdd\u5b58\u5230\u6e90\u6587\u4ef6\u5939\uff09", None))
        self.CroptextRun.setText(QCoreApplication.translate("TextProcWidget", u"\u8fd0\u884c", None))
        self.TextProcChildTab.setTabText(self.TextProcChildTab.indexOf(self.CropText), QCoreApplication.translate("TextProcWidget", u"\u622a\u53d6\u6587\u672c", None))
#if QT_CONFIG(tooltip)
        self.TextProcChildTab.setTabToolTip(self.TextProcChildTab.indexOf(self.CropText), QCoreApplication.translate("TextProcWidget", u"\u622a\u53d6\u6587\u672c\u7684\u5c3e\u90e8\n"
"\u901a\u5e38\u7528\u4e8e\u91cd\u8981\u5185\u5bb9\u5728\u6587\u672c\u5c3e\u90e8\u7684\u60c5\u51b5\uff0c\u5982\u62a5\u9519\u65f6\u7684\u65e5\u5fd7", None))
#endif // QT_CONFIG(tooltip)
        self.CalSimModelDropdown.setPlaceholderText(QCoreApplication.translate("TextProcWidget", u"\u9700\u8981\u5237\u65b0", None))
        self.CalSimModelRefresh.setText(QCoreApplication.translate("TextProcWidget", u"\u5237\u65b0", None))
        self.CalSimPersistentModel.setText(QCoreApplication.translate("TextProcWidget", u"\u6301\u4e45\u6a21\u578b", None))
        self.CalSimIn1.setPlaceholderText(QCoreApplication.translate("TextProcWidget", u"\u8f93\u5165\u6587\u672c 1", None))
        self.CalSimIn2.setPlaceholderText(QCoreApplication.translate("TextProcWidget", u"\u8f93\u5165\u6587\u672c 2", None))
        self.CalSimRun.setText(QCoreApplication.translate("TextProcWidget", u"\u8ba1\u7b97", None))
        self.CalSimUnload.setText(QCoreApplication.translate("TextProcWidget", u"\u5378\u8f7d\u6a21\u578b", None))
        self.TextProcChildTab.setTabText(self.TextProcChildTab.indexOf(self.CalSim), QCoreApplication.translate("TextProcWidget", u"\u8ba1\u7b97\u76f8\u4f3c\u5ea6", None))
#if QT_CONFIG(tooltip)
        self.TextProcChildTab.setTabToolTip(self.TextProcChildTab.indexOf(self.CalSim), QCoreApplication.translate("TextProcWidget", u"\u4f7f\u7528\u5d4c\u5165\u6a21\u578b\u8ba1\u7b97\u4e24\u4e2a\u5b57\u7b26\u4e32\u7684\u8bed\u4e49\u76f8\u4f3c\u5ea6", None))
#endif // QT_CONFIG(tooltip)
        self.JsonSorterInOpen.setText(QCoreApplication.translate("TextProcWidget", u"\u6253\u5f00", None))
        self.JsonSorterInPath.setPlaceholderText(QCoreApplication.translate("TextProcWidget", u"\u8f93\u5165\u6587\u4ef6\u8def\u5f84", None))
        self.JsonSorterRun.setText(QCoreApplication.translate("TextProcWidget", u"\u8fd0\u884c", None))
        self.TextProcChildTab.setTabText(self.TextProcChildTab.indexOf(self.JsonSorter), QCoreApplication.translate("TextProcWidget", u"JSON \u6392\u5e8f", None))
#if QT_CONFIG(tooltip)
        self.TextProcChildTab.setTabToolTip(self.TextProcChildTab.indexOf(self.JsonSorter), QCoreApplication.translate("TextProcWidget", u"\u5c06JSON\u7684\u952e\u503c\u5bf9\u6309\u952e\u7684\u987a\u5e8f\u6392\u5e8f", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

