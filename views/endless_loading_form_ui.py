# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'endless_loading_form.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QProgressBar, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_EndlessLoadingForm(object):
    def setupUi(self, EndlessLoadingForm):
        if not EndlessLoadingForm.objectName():
            EndlessLoadingForm.setObjectName(u"EndlessLoadingForm")
        EndlessLoadingForm.resize(782, 300)
        self.verticalLayout = QVBoxLayout(EndlessLoadingForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.start_progress_bar_btn = QPushButton(EndlessLoadingForm)
        self.start_progress_bar_btn.setObjectName(u"start_progress_bar_btn")

        self.horizontalLayout.addWidget(self.start_progress_bar_btn)

        self.endless_progressBar = QProgressBar(EndlessLoadingForm)
        self.endless_progressBar.setObjectName(u"endless_progressBar")
        self.endless_progressBar.setValue(0)

        self.horizontalLayout.addWidget(self.endless_progressBar)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 248, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(EndlessLoadingForm)

        QMetaObject.connectSlotsByName(EndlessLoadingForm)
    # setupUi

    def retranslateUi(self, EndlessLoadingForm):
        EndlessLoadingForm.setWindowTitle(QCoreApplication.translate("EndlessLoadingForm", u"Form", None))
        self.start_progress_bar_btn.setText(QCoreApplication.translate("EndlessLoadingForm", u"\u0417\u0430\u043f\u0443\u0441\u043a", None))
    # retranslateUi

