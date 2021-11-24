# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'date_form.ui'
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_DateForm(object):
    def setupUi(self, DateForm):
        if not DateForm.objectName():
            DateForm.setObjectName(u"DateForm")
        DateForm.resize(377, 419)
        self.verticalLayout = QVBoxLayout(DateForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(DateForm)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(16)
        self.label_3.setFont(font)

        self.verticalLayout.addWidget(self.label_3)

        self.calendar = QCalendarWidget(DateForm)
        self.calendar.setObjectName(u"calendar")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calendar.sizePolicy().hasHeightForWidth())
        self.calendar.setSizePolicy(sizePolicy)
        self.calendar.setGridVisible(False)
        self.calendar.setSelectionMode(QCalendarWidget.SingleSelection)
        self.calendar.setHorizontalHeaderFormat(QCalendarWidget.ShortDayNames)
        self.calendar.setVerticalHeaderFormat(QCalendarWidget.ISOWeekNumbers)

        self.verticalLayout.addWidget(self.calendar)

        self.day_passed_label = QLabel(DateForm)
        self.day_passed_label.setObjectName(u"day_passed_label")
        sizePolicy.setHeightForWidth(self.day_passed_label.sizePolicy().hasHeightForWidth())
        self.day_passed_label.setSizePolicy(sizePolicy)
        self.day_passed_label.setMinimumSize(QSize(0, 80))
        self.day_passed_label.setFont(font)

        self.verticalLayout.addWidget(self.day_passed_label)


        self.retranslateUi(DateForm)

        QMetaObject.connectSlotsByName(DateForm)
    # setupUi

    def retranslateUi(self, DateForm):
        DateForm.setWindowTitle(QCoreApplication.translate("DateForm", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("DateForm", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0434\u0430\u0442\u0443:", None))
        self.day_passed_label.setText("")
    # retranslateUi

