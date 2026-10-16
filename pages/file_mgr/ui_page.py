# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pageRUhCpK.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QProgressBar,
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_FileMgrWidget(object):
    def setupUi(self, FileMgrWidget):
        if not FileMgrWidget.objectName():
            FileMgrWidget.setObjectName(u"FileMgrWidget")
        FileMgrWidget.resize(725, 666)
        self.verticalLayout = QVBoxLayout(FileMgrWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.FileMgrChildTab = QTabWidget(FileMgrWidget)
        self.FileMgrChildTab.setObjectName(u"FileMgrChildTab")
        self.FileMgrChildTab.setMovable(True)
        self.FlattenLayout = QWidget()
        self.FlattenLayout.setObjectName(u"FlattenLayout")
        self.verticalLayout_17 = QVBoxLayout(self.FlattenLayout)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.FlattenDir = QHBoxLayout()
        self.FlattenDir.setObjectName(u"FlattenDir")
        self.FlattenDirOpen = QPushButton(self.FlattenLayout)
        self.FlattenDirOpen.setObjectName(u"FlattenDirOpen")

        self.FlattenDir.addWidget(self.FlattenDirOpen)

        self.FlattenDirInput = QLineEdit(self.FlattenLayout)
        self.FlattenDirInput.setObjectName(u"FlattenDirInput")
        self.FlattenDirInput.setClearButtonEnabled(True)

        self.FlattenDir.addWidget(self.FlattenDirInput)


        self.verticalLayout_17.addLayout(self.FlattenDir)

        self.FlattenProgress = QProgressBar(self.FlattenLayout)
        self.FlattenProgress.setObjectName(u"FlattenProgress")
        self.FlattenProgress.setValue(0)
        self.FlattenProgress.setTextVisible(False)

        self.verticalLayout_17.addWidget(self.FlattenProgress)

        self.FlattenBtns = QHBoxLayout()
        self.FlattenBtns.setObjectName(u"FlattenBtns")
        self.FlattenRun = QPushButton(self.FlattenLayout)
        self.FlattenRun.setObjectName(u"FlattenRun")

        self.FlattenBtns.addWidget(self.FlattenRun)

        self.FlattenStop = QPushButton(self.FlattenLayout)
        self.FlattenStop.setObjectName(u"FlattenStop")
        self.FlattenStop.setEnabled(False)

        self.FlattenBtns.addWidget(self.FlattenStop)


        self.verticalLayout_17.addLayout(self.FlattenBtns)

        self.FlattenSpacer = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_17.addItem(self.FlattenSpacer)

        self.FileMgrChildTab.addTab(self.FlattenLayout, "")

        self.verticalLayout.addWidget(self.FileMgrChildTab)


        self.retranslateUi(FileMgrWidget)

        self.FileMgrChildTab.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(FileMgrWidget)
    # setupUi

    def retranslateUi(self, FileMgrWidget):
        FileMgrWidget.setWindowTitle(QCoreApplication.translate("FileMgrWidget", u"Form", None))
        self.FlattenDirOpen.setText(QCoreApplication.translate("FileMgrWidget", u"\u6253\u5f00", None))
        self.FlattenDirInput.setPlaceholderText(QCoreApplication.translate("FileMgrWidget", u"\u4ece\u6b64\u5904\u5f00\u59cb\u67e5\u627e\u6587\u4ef6\u5939", None))
        self.FlattenRun.setText(QCoreApplication.translate("FileMgrWidget", u"\u8fd0\u884c", None))
        self.FlattenStop.setText(QCoreApplication.translate("FileMgrWidget", u"\u7ec8\u6b62", None))
        self.FileMgrChildTab.setTabText(self.FileMgrChildTab.indexOf(self.FlattenLayout), QCoreApplication.translate("FileMgrWidget", u"\u5c55\u5e73", None))
#if QT_CONFIG(tooltip)
        self.FileMgrChildTab.setTabToolTip(self.FileMgrChildTab.indexOf(self.FlattenLayout), QCoreApplication.translate("FileMgrWidget", u"\u57fa\u4e8e\u6811\u7684\u65b0\u5c55\u5e73\u65b9\u5f0f\uff0c\u4ee5\u5185\u5b58\u5360\u7528\u4e3a\u4ee3\u4ef7\uff0c\u63d0\u9ad8\u5c55\u5e73\u901f\u5ea6", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

