# -*- coding: utf-8 -*-
import datetime
import sys

from PySide6.QtCore import QTimer, Qt, QDate
from PySide6.QtWidgets import QApplication, QMainWindow

from ui.design import Ui_MainWindow

PIN_CODE = "1234"

HELLO_WORLD_TEXT = {
    "English": "Hello, world!",
    "Русский": "Привет, мир!",
    "Español": "¡Hola Mundo!",
    "Deutsch": "Hallo Welt!",
    "Français": "Bonjour le monde!",
}


# noinspection PyAttributeOutsideInit
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.pin_init()

        self.hello_init()

        self.date_init()

        self.hello_user_init()

        self.endless_loading_init()

    # region Pin

    def pin_init(self):
        self.ui.cat_image.hide()

        self.pin_digit_buttons = (self.ui.pin_btn_1, self.ui.pin_btn_2, self.ui.pin_btn_3,
                                  self.ui.pin_btn_4, self.ui.pin_btn_5, self.ui.pin_btn_6,
                                  self.ui.pin_btn_7, self.ui.pin_btn_8, self.ui.pin_btn_9,
                                  self.ui.pin_btn_0)

        for btn in self.pin_digit_buttons:
            btn.clicked.connect(self.pin_digit)

        self.ui.pin_btn_clr.clicked.connect(self.pin_clr)
        self.ui.pin_btn_enter.clicked.connect(self.pin_enter)

    def hide_pin(self):
        for btn in self.pin_digit_buttons:
            btn.hide()
        self.ui.pin_btn_enter.hide()
        self.ui.pin_btn_clr.hide()

    def show_pin(self):
        for btn in self.pin_digit_buttons:
            btn.show()
        self.ui.pin_btn_enter.show()
        self.ui.pin_btn_clr.show()

    def pin_digit(self):
        btn = self.sender()
        if len(self.ui.pincode_label.text()) < 4:
            self.ui.pincode_label.setText(self.ui.pincode_label.text() + btn.text())

    def pin_clr(self):
        self.ui.cat_image.hide()
        if self.ui.pincode_label.text() == "":
            self.ui.pin_btn_clr.setText("rly?")
        else:
            self.ui.pin_btn_clr.setText("CLR")
            self.ui.pincode_label.setText("")

    def pin_enter(self):
        entered = self.ui.pincode_label.text()
        if entered == PIN_CODE:
            self.ui.cat_image.show()
        else:
            def return_pin():
                self.show_pin()
                self.ui.pincode_label.setText("")

            self.hide_pin()
            self.ui.pincode_label.setText("ERROR")
            QTimer.singleShot(1000, return_pin)

    # endregion

    # region Hello, world!

    def hello_init(self):
        self.hello_straight_text = True

        for (k, _) in HELLO_WORLD_TEXT.items():
            self.ui.language_comboBox.addItem(k)
        self.ui.language_comboBox.currentTextChanged.connect(self.hello_on_language_change)
        self.ui.language_comboBox.setCurrentIndex(0)
        self.ui.hello_label.setText(HELLO_WORLD_TEXT["English"])

        self.ui.bold_checkBox.stateChanged.connect(self.hello_on_font_change)
        self.ui.italic_checkBox.stateChanged.connect(self.hello_on_font_change)
        self.ui.underline_checkBox.stateChanged.connect(self.hello_on_font_change)

        self.ui.fontSize_label.setText(str(self.ui.fontSize_slideBar.value()))
        self.ui.fontSize_slideBar.valueChanged.connect(self.hello_on_font_change)
        self.ui.font_ComboBox.setCurrentFont("Arial")
        self.ui.font_ComboBox.currentFontChanged.connect(self.hello_on_font_change)

        self.ui.straight_radioButton.setChecked(True)
        self.ui.straight_radioButton.toggled.connect(self.hello_on_letter_order_change)
        self.ui.reversed_radioButton.toggled.connect(self.hello_on_letter_order_change)

    def hello_on_language_change(self):
        lang = self.ui.language_comboBox.currentText()
        text = HELLO_WORLD_TEXT.get(lang, "Something went wrong")
        text = text if self.hello_straight_text else text[::-1]
        self.ui.hello_label.setText(text)

    def hello_on_font_change(self):
        sender = self.sender()
        font = self.ui.hello_label.font()

        match sender:
            case self.ui.bold_checkBox:
                font.setBold(self.ui.bold_checkBox.checkState() == Qt.CheckState.Checked)
            case self.ui.italic_checkBox:
                font.setItalic(self.ui.italic_checkBox.checkState() == Qt.CheckState.Checked)
            case self.ui.underline_checkBox:
                font.setUnderline(self.ui.underline_checkBox.checkState() == Qt.CheckState.Checked)
            case self.ui.fontSize_slideBar:
                value = self.ui.fontSize_slideBar.value()
                font.setPointSize(value)
                self.ui.fontSize_label.setText(str(value))
            case self.ui.font_ComboBox:
                font.setFamily(self.ui.font_ComboBox.currentFont().family())

        self.ui.hello_label.setFont(font)

    def hello_on_letter_order_change(self):
        sender = self.sender()
        match sender:
            case self.ui.straight_radioButton:
                if self.ui.straight_radioButton.isChecked():
                    if not self.hello_straight_text:
                        self.hello_straight_text = True
                        self.ui.hello_label.setText(self.ui.hello_label.text()[::-1])

            case self.ui.reversed_radioButton:
                if self.ui.reversed_radioButton.isChecked():
                    if self.hello_straight_text:
                        self.hello_straight_text = False
                        self.ui.hello_label.setText(self.ui.hello_label.text()[::-1])

    # endregion

    # region Date

    def date_init(self):
        self.ui.calendar.selectionChanged.connect(self.date_changed)
        self.ui.calendar.setSelectedDate(QDate.currentDate())

    def date_changed(self):
        selected_date: QDate = self.ui.calendar.selectedDate()
        date = datetime.date(selected_date.year(), selected_date.month(), selected_date.day())
        current_date = date.today()
        delta = current_date - date

        if delta != abs(delta):
            self.ui.day_passed_label.setText(f"До выбранного дня осталось: {abs(delta.days)} дней")
        else:
            self.ui.day_passed_label.setText(f"С выбранного дня прошло: {abs(delta.days)} дней")

    # endregion

    # region Hello, %username%

    def hello_user_init(self):
        self.ui.name_lineEdit.textChanged.connect(self.hello_user_change)

    def hello_user_change(self):
        name = self.ui.name_lineEdit.text().strip()
        if name == "":
            name = "%username%"

        self.ui.helloUser_label.setText(f"Hello, {name}")

    # endregion

    # region Endless loading

    def endless_loading_init(self):
        self.ui.start_progress_bar_btn.pressed.connect(self.endless_loading_start)

    def endless_loading_start(self):
        self.ui.endless_progressBar.setValue(80)
        QTimer.singleShot(60 * 1000, lambda: self.ui.endless_progressBar.setValue(100))

    # endregion


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
