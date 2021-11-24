# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'price_form.ui'
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFormLayout, QLabel,
    QLineEdit, QSizePolicy, QSpinBox, QWidget)

class Ui_PriceForm(object):
    def setupUi(self, PriceForm):
        if not PriceForm.objectName():
            PriceForm.setObjectName(u"PriceForm")
        PriceForm.resize(283, 300)
        self.formLayout = QFormLayout(PriceForm)
        self.formLayout.setObjectName(u"formLayout")
        self.label_5 = QLabel(PriceForm)
        self.label_5.setObjectName(u"label_5")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_5)

        self.price_spinBox = QDoubleSpinBox(PriceForm)
        self.price_spinBox.setObjectName(u"price_spinBox")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.price_spinBox)

        self.label_6 = QLabel(PriceForm)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_6)

        self.count_spinBox = QSpinBox(PriceForm)
        self.count_spinBox.setObjectName(u"count_spinBox")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.count_spinBox)

        self.label_7 = QLabel(PriceForm)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_7)

        self.total_lineEdit = QLineEdit(PriceForm)
        self.total_lineEdit.setObjectName(u"total_lineEdit")
        sizePolicy.setHeightForWidth(self.total_lineEdit.sizePolicy().hasHeightForWidth())
        self.total_lineEdit.setSizePolicy(sizePolicy)
        self.total_lineEdit.setFrame(True)
        self.total_lineEdit.setReadOnly(True)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.total_lineEdit)


        self.retranslateUi(PriceForm)

        QMetaObject.connectSlotsByName(PriceForm)
    # setupUi

    def retranslateUi(self, PriceForm):
        PriceForm.setWindowTitle(QCoreApplication.translate("PriceForm", u"Form", None))
        self.label_5.setText(QCoreApplication.translate("PriceForm", u"\u0426\u0435\u043d\u0430", None))
        self.label_6.setText(QCoreApplication.translate("PriceForm", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.label_7.setText(QCoreApplication.translate("PriceForm", u"\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c", None))
    # retranslateUi

