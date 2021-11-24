# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hello_world_form.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFontComboBox,
    QGroupBox, QHBoxLayout, QLabel, QRadioButton,
    QSizePolicy, QSlider, QVBoxLayout, QWidget)

class Ui_HelloWorldForm(object):
    def setupUi(self, HelloWorldForm):
        if not HelloWorldForm.objectName():
            HelloWorldForm.setObjectName(u"HelloWorldForm")
        HelloWorldForm.resize(500, 375)
        self.verticalLayout = QVBoxLayout(HelloWorldForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(HelloWorldForm)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.language_comboBox = QComboBox(HelloWorldForm)
        self.language_comboBox.setObjectName(u"language_comboBox")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(16)
        self.language_comboBox.setFont(font1)
        self.language_comboBox.setEditable(False)

        self.verticalLayout.addWidget(self.language_comboBox)

        self.hello_label = QLabel(HelloWorldForm)
        self.hello_label.setObjectName(u"hello_label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hello_label.sizePolicy().hasHeightForWidth())
        self.hello_label.setSizePolicy(sizePolicy)
        self.hello_label.setMinimumSize(QSize(0, 80))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(8)
        self.hello_label.setFont(font2)

        self.verticalLayout.addWidget(self.hello_label)

        self.groupBox = QGroupBox(HelloWorldForm)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.verticalLayout_5 = QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.bold_checkBox = QCheckBox(self.groupBox)
        self.bold_checkBox.setObjectName(u"bold_checkBox")

        self.verticalLayout_2.addWidget(self.bold_checkBox)

        self.italic_checkBox = QCheckBox(self.groupBox)
        self.italic_checkBox.setObjectName(u"italic_checkBox")

        self.verticalLayout_2.addWidget(self.italic_checkBox)

        self.underline_checkBox = QCheckBox(self.groupBox)
        self.underline_checkBox.setObjectName(u"underline_checkBox")

        self.verticalLayout_2.addWidget(self.underline_checkBox)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.fontSize_label = QLabel(self.groupBox)
        self.fontSize_label.setObjectName(u"fontSize_label")

        self.verticalLayout_4.addWidget(self.fontSize_label)

        self.fontSize_slideBar = QSlider(self.groupBox)
        self.fontSize_slideBar.setObjectName(u"fontSize_slideBar")
        self.fontSize_slideBar.setMinimum(8)
        self.fontSize_slideBar.setMaximum(32)
        self.fontSize_slideBar.setOrientation(Qt.Horizontal)
        self.fontSize_slideBar.setInvertedControls(False)
        self.fontSize_slideBar.setTickPosition(QSlider.TicksAbove)
        self.fontSize_slideBar.setTickInterval(2)

        self.verticalLayout_4.addWidget(self.fontSize_slideBar)


        self.horizontalLayout.addLayout(self.verticalLayout_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.font_ComboBox = QFontComboBox(self.groupBox)
        self.font_ComboBox.setObjectName(u"font_ComboBox")

        self.verticalLayout_5.addWidget(self.font_ComboBox)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(HelloWorldForm)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy2)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.straight_radioButton = QRadioButton(self.groupBox_2)
        self.straight_radioButton.setObjectName(u"straight_radioButton")

        self.verticalLayout_3.addWidget(self.straight_radioButton)

        self.reversed_radioButton = QRadioButton(self.groupBox_2)
        self.reversed_radioButton.setObjectName(u"reversed_radioButton")

        self.verticalLayout_3.addWidget(self.reversed_radioButton)


        self.verticalLayout.addWidget(self.groupBox_2)


        self.retranslateUi(HelloWorldForm)

        QMetaObject.connectSlotsByName(HelloWorldForm)
    # setupUi

    def retranslateUi(self, HelloWorldForm):
        HelloWorldForm.setWindowTitle(QCoreApplication.translate("HelloWorldForm", u"Form", None))
        self.label.setText(QCoreApplication.translate("HelloWorldForm", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u044f\u0437\u044b\u043a:", None))
        self.hello_label.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("HelloWorldForm", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0448\u0440\u0438\u0444\u0442\u0430", None))
        self.bold_checkBox.setText(QCoreApplication.translate("HelloWorldForm", u"\u0416\u0438\u0440\u043d\u044b\u0439", None))
        self.italic_checkBox.setText(QCoreApplication.translate("HelloWorldForm", u"\u041a\u0443\u0440\u0441\u0438\u0432", None))
        self.underline_checkBox.setText(QCoreApplication.translate("HelloWorldForm", u"\u041f\u043e\u0434\u0447\u0451\u0440\u043a\u043d\u0443\u0442\u044b\u0439", None))
        self.fontSize_label.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("HelloWorldForm", u"\u041f\u043e\u0440\u044f\u0434\u043e\u043a \u0431\u0443\u043a\u0432", None))
        self.straight_radioButton.setText(QCoreApplication.translate("HelloWorldForm", u"\u041f\u0440\u044f\u043c\u043e\u0439", None))
        self.reversed_radioButton.setText(QCoreApplication.translate("HelloWorldForm", u"\u041e\u0431\u0440\u0430\u0442\u043d\u044b\u0439", None))
    # retranslateUi

