# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hello_user_form.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_HelloUserForm(object):
    def setupUi(self, HelloUserForm):
        if not HelloUserForm.objectName():
            HelloUserForm.setObjectName(u"HelloUserForm")
        HelloUserForm.resize(400, 243)
        self.verticalLayout = QVBoxLayout(HelloUserForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_4 = QLabel(HelloUserForm)
        self.label_4.setObjectName(u"label_4")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(16)
        self.label_4.setFont(font)

        self.verticalLayout.addWidget(self.label_4)

        self.name_lineEdit = QLineEdit(HelloUserForm)
        self.name_lineEdit.setObjectName(u"name_lineEdit")
        self.name_lineEdit.setFont(font)

        self.verticalLayout.addWidget(self.name_lineEdit)

        self.helloUser_label = QLabel(HelloUserForm)
        self.helloUser_label.setObjectName(u"helloUser_label")
        sizePolicy.setHeightForWidth(self.helloUser_label.sizePolicy().hasHeightForWidth())
        self.helloUser_label.setSizePolicy(sizePolicy)
        self.helloUser_label.setFont(font)

        self.verticalLayout.addWidget(self.helloUser_label)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(HelloUserForm)

        QMetaObject.connectSlotsByName(HelloUserForm)
    # setupUi

    def retranslateUi(self, HelloUserForm):
        HelloUserForm.setWindowTitle(QCoreApplication.translate("HelloUserForm", u"Form", None))
        self.label_4.setText(QCoreApplication.translate("HelloUserForm", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0441\u0432\u043e\u0435 \u0438\u043c\u044f:", None))
        self.helloUser_label.setText(QCoreApplication.translate("HelloUserForm", u"Hello, %username%", None))
    # retranslateUi

