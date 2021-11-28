# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pin_code_form.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QWidget)
import assets_rc

class Ui_PinCodeForm(object):
    def setupUi(self, PinCodeForm):
        if not PinCodeForm.objectName():
            PinCodeForm.setObjectName(u"PinCodeForm")
        PinCodeForm.resize(1357, 618)
        self.horizontalLayout = QHBoxLayout(PinCodeForm)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pin_btn_2 = QPushButton(PinCodeForm)
        self.pin_btn_2.setObjectName(u"pin_btn_2")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pin_btn_2.sizePolicy().hasHeightForWidth())
        self.pin_btn_2.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(14)
        self.pin_btn_2.setFont(font)

        self.gridLayout.addWidget(self.pin_btn_2, 2, 1, 1, 1)

        self.pin_btn_5 = QPushButton(PinCodeForm)
        self.pin_btn_5.setObjectName(u"pin_btn_5")
        sizePolicy.setHeightForWidth(self.pin_btn_5.sizePolicy().hasHeightForWidth())
        self.pin_btn_5.setSizePolicy(sizePolicy)
        self.pin_btn_5.setFont(font)

        self.gridLayout.addWidget(self.pin_btn_5, 3, 1, 1, 1)

        self.pin_btn_3 = QPushButton(PinCodeForm)
        self.pin_btn_3.setObjectName(u"pin_btn_3")
        sizePolicy.setHeightForWidth(self.pin_btn_3.sizePolicy().hasHeightForWidth())
        self.pin_btn_3.setSizePolicy(sizePolicy)
        self.pin_btn_3.setFont(font)

        self.gridLayout.addWidget(self.pin_btn_3, 2, 2, 1, 1)

        self.pin_btn_4 = QPushButton(PinCodeForm)
        self.pin_btn_4.setObjectName(u"pin_btn_4")
        sizePolicy.setHeightForWidth(self.pin_btn_4.sizePolicy().hasHeightForWidth())
        self.pin_btn_4.setSizePolicy(sizePolicy)
        self.pin_btn_4.setFont(font)

        self.gridLayout.addWidget(self.pin_btn_4, 3, 0, 1, 1)

        self.pin_btn_6 = QPushButton(PinCodeForm)
        self.pin_btn_6.setObjectName(u"pin_btn_6")
        sizePolicy.setHeightForWidth(self.pin_btn_6.sizePolicy().hasHeightForWidth())
        self.pin_btn_6.setSizePolicy(sizePolicy)
        self.pin_btn_6.setFont(font)

        self.gridLayout.addWidget(self.pin_btn_6, 3, 2, 1, 1)

        self.label_2 = QLabel(PinCodeForm)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(16)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 3)

        self.pin_btn_enter = QPushButton(PinCodeForm)
        self.pin_btn_enter.setObjectName(u"pin_btn_enter")
        sizePolicy.setHeightForWidth(self.pin_btn_enter.sizePolicy().hasHeightForWidth())
        self.pin_btn_enter.setSizePolicy(sizePolicy)
        self.pin_btn_enter.setFont(font)

        self.gridLayout.addWidget(self.pin_btn_enter, 5, 2, 1, 1)

        self.pin_btn_1 = QPushButton(PinCodeForm)
        self.pin_btn_1.setObjectName(u"pin_btn_1")
        sizePolicy.setHeightForWidth(self.pin_btn_1.sizePolicy().hasHeightForWidth())
        self.pin_btn_1.setSizePolicy(sizePolicy)
        self.pin_btn_1.setSizeIncrement(QSize(1, 1))
        self.pin_btn_1.setFont(font)

        self.gridLayout.addWidget(self.pin_btn_1, 2, 0, 1, 1)

        self.pincode_label = QLabel(PinCodeForm)
        self.pincode_label.setObjectName(u"pincode_label")
        sizePolicy1.setHeightForWidth(self.pincode_label.sizePolicy().hasHeightForWidth())
        self.pincode_label.setSizePolicy(sizePolicy1)
        self.pincode_label.setFont(font1)
        self.pincode_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.pincode_label, 1, 0, 1, 3)

        self.pin_btn_clr = QPushButton(PinCodeForm)
        self.pin_btn_clr.setObjectName(u"pin_btn_clr")
        sizePolicy.setHeightForWidth(self.pin_btn_clr.sizePolicy().hasHeightForWidth())
        self.pin_btn_clr.setSizePolicy(sizePolicy)
        self.pin_btn_clr.setFont(font)

        self.gridLayout.addWidget(self.pin_btn_clr, 5, 0, 1, 1)

        self.pin_btn_7 = QPushButton(PinCodeForm)
        self.pin_btn_7.setObjectName(u"pin_btn_7")
        sizePolicy.setHeightForWidth(self.pin_btn_7.sizePolicy().hasHeightForWidth())
        self.pin_btn_7.setSizePolicy(sizePolicy)
        self.pin_btn_7.setFont(font)

        self.gridLayout.addWidget(self.pin_btn_7, 4, 0, 1, 1)

        self.pin_btn_8 = QPushButton(PinCodeForm)
        self.pin_btn_8.setObjectName(u"pin_btn_8")
        sizePolicy.setHeightForWidth(self.pin_btn_8.sizePolicy().hasHeightForWidth())
        self.pin_btn_8.setSizePolicy(sizePolicy)
        self.pin_btn_8.setFont(font)

        self.gridLayout.addWidget(self.pin_btn_8, 4, 1, 1, 1)

        self.pin_btn_0 = QPushButton(PinCodeForm)
        self.pin_btn_0.setObjectName(u"pin_btn_0")
        sizePolicy.setHeightForWidth(self.pin_btn_0.sizePolicy().hasHeightForWidth())
        self.pin_btn_0.setSizePolicy(sizePolicy)
        self.pin_btn_0.setFont(font)

        self.gridLayout.addWidget(self.pin_btn_0, 5, 1, 1, 1)

        self.pin_btn_9 = QPushButton(PinCodeForm)
        self.pin_btn_9.setObjectName(u"pin_btn_9")
        sizePolicy.setHeightForWidth(self.pin_btn_9.sizePolicy().hasHeightForWidth())
        self.pin_btn_9.setSizePolicy(sizePolicy)
        self.pin_btn_9.setFont(font)

        self.gridLayout.addWidget(self.pin_btn_9, 4, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 6, 0, 1, 3)


        self.horizontalLayout.addLayout(self.gridLayout)


        self.retranslateUi(PinCodeForm)

        QMetaObject.connectSlotsByName(PinCodeForm)
    # setupUi

    def retranslateUi(self, PinCodeForm):
        PinCodeForm.setWindowTitle(QCoreApplication.translate("PinCodeForm", u"Form", None))
        self.pin_btn_2.setText(QCoreApplication.translate("PinCodeForm", u"2", None))
#if QT_CONFIG(shortcut)
        self.pin_btn_2.setShortcut(QCoreApplication.translate("PinCodeForm", u"2", None))
#endif // QT_CONFIG(shortcut)
        self.pin_btn_5.setText(QCoreApplication.translate("PinCodeForm", u"5", None))
#if QT_CONFIG(shortcut)
        self.pin_btn_5.setShortcut(QCoreApplication.translate("PinCodeForm", u"5", None))
#endif // QT_CONFIG(shortcut)
        self.pin_btn_3.setText(QCoreApplication.translate("PinCodeForm", u"3", None))
#if QT_CONFIG(shortcut)
        self.pin_btn_3.setShortcut(QCoreApplication.translate("PinCodeForm", u"3", None))
#endif // QT_CONFIG(shortcut)
        self.pin_btn_4.setText(QCoreApplication.translate("PinCodeForm", u"4", None))
#if QT_CONFIG(shortcut)
        self.pin_btn_4.setShortcut(QCoreApplication.translate("PinCodeForm", u"4", None))
#endif // QT_CONFIG(shortcut)
        self.pin_btn_6.setText(QCoreApplication.translate("PinCodeForm", u"6", None))
#if QT_CONFIG(shortcut)
        self.pin_btn_6.setShortcut(QCoreApplication.translate("PinCodeForm", u"6", None))
#endif // QT_CONFIG(shortcut)
        self.label_2.setText(QCoreApplication.translate("PinCodeForm", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0438\u043d\u043a\u043e\u0434:", None))
        self.pin_btn_enter.setText(QCoreApplication.translate("PinCodeForm", u"ENTER", None))
#if QT_CONFIG(shortcut)
        self.pin_btn_enter.setShortcut(QCoreApplication.translate("PinCodeForm", u"Enter", None))
#endif // QT_CONFIG(shortcut)
        self.pin_btn_1.setText(QCoreApplication.translate("PinCodeForm", u"1", None))
#if QT_CONFIG(shortcut)
        self.pin_btn_1.setShortcut(QCoreApplication.translate("PinCodeForm", u"1", None))
#endif // QT_CONFIG(shortcut)
        self.pincode_label.setText("")
        self.pin_btn_clr.setText(QCoreApplication.translate("PinCodeForm", u"CLR", None))
#if QT_CONFIG(shortcut)
        self.pin_btn_clr.setShortcut(QCoreApplication.translate("PinCodeForm", u"Backspace", None))
#endif // QT_CONFIG(shortcut)
        self.pin_btn_7.setText(QCoreApplication.translate("PinCodeForm", u"7", None))
#if QT_CONFIG(shortcut)
        self.pin_btn_7.setShortcut(QCoreApplication.translate("PinCodeForm", u"7", None))
#endif // QT_CONFIG(shortcut)
        self.pin_btn_8.setText(QCoreApplication.translate("PinCodeForm", u"8", None))
#if QT_CONFIG(shortcut)
        self.pin_btn_8.setShortcut(QCoreApplication.translate("PinCodeForm", u"8", None))
#endif // QT_CONFIG(shortcut)
        self.pin_btn_0.setText(QCoreApplication.translate("PinCodeForm", u"0", None))
#if QT_CONFIG(shortcut)
        self.pin_btn_0.setShortcut(QCoreApplication.translate("PinCodeForm", u"0", None))
#endif // QT_CONFIG(shortcut)
        self.pin_btn_9.setText(QCoreApplication.translate("PinCodeForm", u"9", None))
#if QT_CONFIG(shortcut)
        self.pin_btn_9.setShortcut(QCoreApplication.translate("PinCodeForm", u"9", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

