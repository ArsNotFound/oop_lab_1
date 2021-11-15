# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QCheckBox, QComboBox,
    QFontComboBox, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QProgressBar,
    QPushButton, QRadioButton, QSizePolicy, QSlider,
    QTabWidget, QVBoxLayout, QWidget)
from  . import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1040, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 1040, 600))
        self.pin = QWidget()
        self.pin.setObjectName(u"pin")
        self.cat_image = QLabel(self.pin)
        self.cat_image.setObjectName(u"cat_image")
        self.cat_image.setEnabled(True)
        self.cat_image.setGeometry(QRect(450, 30, 551, 415))
        self.cat_image.setPixmap(QPixmap(u":/image/assets/cat.jpg"))
        self.cat_image.setScaledContents(True)
        self.layoutWidget = QWidget(self.pin)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 30, 301, 441))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pincode_label = QLabel(self.layoutWidget)
        self.pincode_label.setObjectName(u"pincode_label")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pincode_label.sizePolicy().hasHeightForWidth())
        self.pincode_label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(16)
        self.pincode_label.setFont(font)
        self.pincode_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.pincode_label, 1, 0, 1, 3)

        self.pin_btn_8 = QPushButton(self.layoutWidget)
        self.pin_btn_8.setObjectName(u"pin_btn_8")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pin_btn_8.sizePolicy().hasHeightForWidth())
        self.pin_btn_8.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(14)
        self.pin_btn_8.setFont(font1)

        self.gridLayout.addWidget(self.pin_btn_8, 4, 1, 1, 1)

        self.pin_btn_9 = QPushButton(self.layoutWidget)
        self.pin_btn_9.setObjectName(u"pin_btn_9")
        sizePolicy1.setHeightForWidth(self.pin_btn_9.sizePolicy().hasHeightForWidth())
        self.pin_btn_9.setSizePolicy(sizePolicy1)
        self.pin_btn_9.setFont(font1)

        self.gridLayout.addWidget(self.pin_btn_9, 4, 2, 1, 1)

        self.pin_btn_clr = QPushButton(self.layoutWidget)
        self.pin_btn_clr.setObjectName(u"pin_btn_clr")
        sizePolicy1.setHeightForWidth(self.pin_btn_clr.sizePolicy().hasHeightForWidth())
        self.pin_btn_clr.setSizePolicy(sizePolicy1)
        self.pin_btn_clr.setFont(font1)

        self.gridLayout.addWidget(self.pin_btn_clr, 5, 0, 1, 1)

        self.pin_btn_0 = QPushButton(self.layoutWidget)
        self.pin_btn_0.setObjectName(u"pin_btn_0")
        sizePolicy1.setHeightForWidth(self.pin_btn_0.sizePolicy().hasHeightForWidth())
        self.pin_btn_0.setSizePolicy(sizePolicy1)
        self.pin_btn_0.setFont(font1)

        self.gridLayout.addWidget(self.pin_btn_0, 5, 1, 1, 1)

        self.pin_btn_enter = QPushButton(self.layoutWidget)
        self.pin_btn_enter.setObjectName(u"pin_btn_enter")
        sizePolicy1.setHeightForWidth(self.pin_btn_enter.sizePolicy().hasHeightForWidth())
        self.pin_btn_enter.setSizePolicy(sizePolicy1)
        self.pin_btn_enter.setFont(font1)

        self.gridLayout.addWidget(self.pin_btn_enter, 5, 2, 1, 1)

        self.pin_btn_4 = QPushButton(self.layoutWidget)
        self.pin_btn_4.setObjectName(u"pin_btn_4")
        sizePolicy1.setHeightForWidth(self.pin_btn_4.sizePolicy().hasHeightForWidth())
        self.pin_btn_4.setSizePolicy(sizePolicy1)
        self.pin_btn_4.setFont(font1)

        self.gridLayout.addWidget(self.pin_btn_4, 3, 0, 1, 1)

        self.pin_btn_7 = QPushButton(self.layoutWidget)
        self.pin_btn_7.setObjectName(u"pin_btn_7")
        sizePolicy1.setHeightForWidth(self.pin_btn_7.sizePolicy().hasHeightForWidth())
        self.pin_btn_7.setSizePolicy(sizePolicy1)
        self.pin_btn_7.setFont(font1)

        self.gridLayout.addWidget(self.pin_btn_7, 4, 0, 1, 1)

        self.pin_btn_6 = QPushButton(self.layoutWidget)
        self.pin_btn_6.setObjectName(u"pin_btn_6")
        sizePolicy1.setHeightForWidth(self.pin_btn_6.sizePolicy().hasHeightForWidth())
        self.pin_btn_6.setSizePolicy(sizePolicy1)
        self.pin_btn_6.setFont(font1)

        self.gridLayout.addWidget(self.pin_btn_6, 3, 2, 1, 1)

        self.pin_btn_5 = QPushButton(self.layoutWidget)
        self.pin_btn_5.setObjectName(u"pin_btn_5")
        sizePolicy1.setHeightForWidth(self.pin_btn_5.sizePolicy().hasHeightForWidth())
        self.pin_btn_5.setSizePolicy(sizePolicy1)
        self.pin_btn_5.setFont(font1)

        self.gridLayout.addWidget(self.pin_btn_5, 3, 1, 1, 1)

        self.pin_btn_2 = QPushButton(self.layoutWidget)
        self.pin_btn_2.setObjectName(u"pin_btn_2")
        sizePolicy1.setHeightForWidth(self.pin_btn_2.sizePolicy().hasHeightForWidth())
        self.pin_btn_2.setSizePolicy(sizePolicy1)
        self.pin_btn_2.setFont(font1)

        self.gridLayout.addWidget(self.pin_btn_2, 2, 1, 1, 1)

        self.pin_btn_3 = QPushButton(self.layoutWidget)
        self.pin_btn_3.setObjectName(u"pin_btn_3")
        sizePolicy1.setHeightForWidth(self.pin_btn_3.sizePolicy().hasHeightForWidth())
        self.pin_btn_3.setSizePolicy(sizePolicy1)
        self.pin_btn_3.setFont(font1)

        self.gridLayout.addWidget(self.pin_btn_3, 2, 2, 1, 1)

        self.pin_btn_1 = QPushButton(self.layoutWidget)
        self.pin_btn_1.setObjectName(u"pin_btn_1")
        sizePolicy1.setHeightForWidth(self.pin_btn_1.sizePolicy().hasHeightForWidth())
        self.pin_btn_1.setSizePolicy(sizePolicy1)
        self.pin_btn_1.setFont(font1)

        self.gridLayout.addWidget(self.pin_btn_1, 2, 0, 1, 1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 3)

        self.tabWidget.addTab(self.pin, "")
        self.hello = QWidget()
        self.hello.setObjectName(u"hello")
        self.layoutWidget1 = QWidget(self.hello)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(30, 30, 401, 491))
        self.verticalLayout = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setSpacing(16)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget1)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(16)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setUnderline(False)
        self.label.setFont(font2)

        self.verticalLayout.addWidget(self.label)

        self.language_comboBox = QComboBox(self.layoutWidget1)
        self.language_comboBox.setObjectName(u"language_comboBox")
        self.language_comboBox.setFont(font)
        self.language_comboBox.setEditable(False)

        self.verticalLayout.addWidget(self.language_comboBox)

        self.hello_label = QLabel(self.layoutWidget1)
        self.hello_label.setObjectName(u"hello_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.hello_label.sizePolicy().hasHeightForWidth())
        self.hello_label.setSizePolicy(sizePolicy2)
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(8)
        self.hello_label.setFont(font3)

        self.verticalLayout.addWidget(self.hello_label)

        self.groupBox = QGroupBox(self.layoutWidget1)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy3)
        self.layoutWidget2 = QWidget(self.groupBox)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 20, 381, 95))
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.bold_checkBox = QCheckBox(self.layoutWidget2)
        self.bold_checkBox.setObjectName(u"bold_checkBox")

        self.verticalLayout_2.addWidget(self.bold_checkBox)

        self.italic_checkBox = QCheckBox(self.layoutWidget2)
        self.italic_checkBox.setObjectName(u"italic_checkBox")

        self.verticalLayout_2.addWidget(self.italic_checkBox)

        self.underline_checkBox = QCheckBox(self.layoutWidget2)
        self.underline_checkBox.setObjectName(u"underline_checkBox")

        self.verticalLayout_2.addWidget(self.underline_checkBox)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.fontSize_label = QLabel(self.layoutWidget2)
        self.fontSize_label.setObjectName(u"fontSize_label")

        self.verticalLayout_4.addWidget(self.fontSize_label)

        self.fontSize_slideBar = QSlider(self.layoutWidget2)
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

        self.font_ComboBox = QFontComboBox(self.layoutWidget2)
        self.font_ComboBox.setObjectName(u"font_ComboBox")

        self.verticalLayout_5.addWidget(self.font_ComboBox)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.layoutWidget1)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy2.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy2)
        self.layoutWidget3 = QWidget(self.groupBox_2)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(10, 20, 77, 42))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.straight_radioButton = QRadioButton(self.layoutWidget3)
        self.straight_radioButton.setObjectName(u"straight_radioButton")

        self.verticalLayout_3.addWidget(self.straight_radioButton)

        self.reversed_radioButton = QRadioButton(self.layoutWidget3)
        self.reversed_radioButton.setObjectName(u"reversed_radioButton")

        self.verticalLayout_3.addWidget(self.reversed_radioButton)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.tabWidget.addTab(self.hello, "")
        self.date = QWidget()
        self.date.setObjectName(u"date")
        self.widget = QWidget(self.date)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(40, 30, 461, 411))
        self.verticalLayout_6 = QVBoxLayout(self.widget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.verticalLayout_6.addWidget(self.label_3)

        self.calendar = QCalendarWidget(self.widget)
        self.calendar.setObjectName(u"calendar")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.calendar.sizePolicy().hasHeightForWidth())
        self.calendar.setSizePolicy(sizePolicy4)
        self.calendar.setGridVisible(False)
        self.calendar.setSelectionMode(QCalendarWidget.SingleSelection)
        self.calendar.setHorizontalHeaderFormat(QCalendarWidget.ShortDayNames)
        self.calendar.setVerticalHeaderFormat(QCalendarWidget.ISOWeekNumbers)

        self.verticalLayout_6.addWidget(self.calendar)

        self.day_passed_label = QLabel(self.widget)
        self.day_passed_label.setObjectName(u"day_passed_label")
        self.day_passed_label.setFont(font)

        self.verticalLayout_6.addWidget(self.day_passed_label)

        self.verticalLayout_6.setStretch(2, 1)
        self.tabWidget.addTab(self.date, "")
        self.hello_username = QWidget()
        self.hello_username.setObjectName(u"hello_username")
        self.widget1 = QWidget(self.hello_username)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(30, 30, 331, 92))
        self.verticalLayout_7 = QVBoxLayout(self.widget1)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.widget1)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.verticalLayout_7.addWidget(self.label_4)

        self.name_lineEdit = QLineEdit(self.widget1)
        self.name_lineEdit.setObjectName(u"name_lineEdit")
        self.name_lineEdit.setFont(font)

        self.verticalLayout_7.addWidget(self.name_lineEdit)

        self.helloUser_label = QLabel(self.widget1)
        self.helloUser_label.setObjectName(u"helloUser_label")
        self.helloUser_label.setFont(font)

        self.verticalLayout_7.addWidget(self.helloUser_label)

        self.tabWidget.addTab(self.hello_username, "")
        self.endless_loading = QWidget()
        self.endless_loading.setObjectName(u"endless_loading")
        self.widget2 = QWidget(self.endless_loading)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(40, 30, 961, 25))
        self.horizontalLayout_2 = QHBoxLayout(self.widget2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.start_progress_bar_btn = QPushButton(self.widget2)
        self.start_progress_bar_btn.setObjectName(u"start_progress_bar_btn")

        self.horizontalLayout_2.addWidget(self.start_progress_bar_btn)

        self.endless_progressBar = QProgressBar(self.widget2)
        self.endless_progressBar.setObjectName(u"endless_progressBar")
        self.endless_progressBar.setValue(0)

        self.horizontalLayout_2.addWidget(self.endless_progressBar)

        self.tabWidget.addTab(self.endless_loading, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.cat_image.setText("")
        self.pincode_label.setText("")
        self.pin_btn_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
#if QT_CONFIG(shortcut)
        self.pin_btn_8.setShortcut(QCoreApplication.translate("MainWindow", u"8", None))
#endif // QT_CONFIG(shortcut)
        self.pin_btn_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
#if QT_CONFIG(shortcut)
        self.pin_btn_9.setShortcut(QCoreApplication.translate("MainWindow", u"9", None))
#endif // QT_CONFIG(shortcut)
        self.pin_btn_clr.setText(QCoreApplication.translate("MainWindow", u"CLR", None))
#if QT_CONFIG(shortcut)
        self.pin_btn_clr.setShortcut(QCoreApplication.translate("MainWindow", u"Backspace", None))
#endif // QT_CONFIG(shortcut)
        self.pin_btn_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(shortcut)
        self.pin_btn_0.setShortcut(QCoreApplication.translate("MainWindow", u"0", None))
#endif // QT_CONFIG(shortcut)
        self.pin_btn_enter.setText(QCoreApplication.translate("MainWindow", u"ENTER", None))
#if QT_CONFIG(shortcut)
        self.pin_btn_enter.setShortcut(QCoreApplication.translate("MainWindow", u"Enter", None))
#endif // QT_CONFIG(shortcut)
        self.pin_btn_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
#if QT_CONFIG(shortcut)
        self.pin_btn_4.setShortcut(QCoreApplication.translate("MainWindow", u"4", None))
#endif // QT_CONFIG(shortcut)
        self.pin_btn_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
#if QT_CONFIG(shortcut)
        self.pin_btn_7.setShortcut(QCoreApplication.translate("MainWindow", u"7", None))
#endif // QT_CONFIG(shortcut)
        self.pin_btn_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
#if QT_CONFIG(shortcut)
        self.pin_btn_6.setShortcut(QCoreApplication.translate("MainWindow", u"6", None))
#endif // QT_CONFIG(shortcut)
        self.pin_btn_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
#if QT_CONFIG(shortcut)
        self.pin_btn_5.setShortcut(QCoreApplication.translate("MainWindow", u"5", None))
#endif // QT_CONFIG(shortcut)
        self.pin_btn_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
#if QT_CONFIG(shortcut)
        self.pin_btn_2.setShortcut(QCoreApplication.translate("MainWindow", u"2", None))
#endif // QT_CONFIG(shortcut)
        self.pin_btn_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
#if QT_CONFIG(shortcut)
        self.pin_btn_3.setShortcut(QCoreApplication.translate("MainWindow", u"3", None))
#endif // QT_CONFIG(shortcut)
        self.pin_btn_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
#if QT_CONFIG(shortcut)
        self.pin_btn_1.setShortcut(QCoreApplication.translate("MainWindow", u"1", None))
#endif // QT_CONFIG(shortcut)
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0438\u043d\u043a\u043e\u0434:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pin), QCoreApplication.translate("MainWindow", u"Pin Code", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u044f\u0437\u044b\u043a:", None))
        self.hello_label.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0448\u0440\u0438\u0444\u0442\u0430", None))
        self.bold_checkBox.setText(QCoreApplication.translate("MainWindow", u"\u0416\u0438\u0440\u043d\u044b\u0439", None))
        self.italic_checkBox.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0443\u0440\u0441\u0438\u0432", None))
        self.underline_checkBox.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0447\u0451\u0440\u043a\u043d\u0443\u0442\u044b\u0439", None))
        self.fontSize_label.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0440\u044f\u0434\u043e\u043a \u0431\u0443\u043a\u0432", None))
        self.straight_radioButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u044f\u043c\u043e\u0439", None))
        self.reversed_radioButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0440\u0430\u0442\u043d\u044b\u0439", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.hello), QCoreApplication.translate("MainWindow", u"Hello, world!", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0434\u0430\u0442\u0443:", None))
        self.day_passed_label.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.date), QCoreApplication.translate("MainWindow", u"Date", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0441\u0432\u043e\u0435 \u0438\u043c\u044f:", None))
        self.helloUser_label.setText(QCoreApplication.translate("MainWindow", u"Hello, %username%", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.hello_username), QCoreApplication.translate("MainWindow", u"Hello, %username%", None))
        self.start_progress_bar_btn.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u043a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.endless_loading), QCoreApplication.translate("MainWindow", u"Endless loading", None))
    # retranslateUi

