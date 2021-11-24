from typing import Optional

from PySide6.QtCore import Slot, QTimer
from PySide6.QtWidgets import QWidget

from views.pin_code_form_ui import Ui_PinCodeForm

PIN_CODE = "1234"


class PinCodeForm(QWidget):
    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)
        self._ui = Ui_PinCodeForm()
        self._ui.setupUi(self)

        self._ui.cat_image.hide()

        self.pin_digit_buttons = (self._ui.pin_btn_1, self._ui.pin_btn_2, self._ui.pin_btn_3,
                                  self._ui.pin_btn_4, self._ui.pin_btn_5, self._ui.pin_btn_6,
                                  self._ui.pin_btn_7, self._ui.pin_btn_8, self._ui.pin_btn_9,
                                  self._ui.pin_btn_0)

        for btn in self.pin_digit_buttons:
            btn.clicked.connect(self.pin_digit)

        self._ui.pin_btn_clr.clicked.connect(self.pin_clr)
        self._ui.pin_btn_enter.clicked.connect(self.pin_enter)

    @Slot()
    def pin_digit(self):
        btn = self.sender()
        if len(self._ui.pincode_label.text()) < 4:
            self._ui.pincode_label.setText(self._ui.pincode_label.text() + btn.text())

    @Slot()
    def pin_clr(self):
        self._ui.cat_image.hide()
        if self._ui.pincode_label.text() == "":
            self._ui.pin_btn_clr.setText("rly?")
        else:
            self._ui.pin_btn_clr.setText("CLR")
            self._ui.pincode_label.setText("")

    @Slot()
    def pin_enter(self):
        entered = self._ui.pincode_label.text()
        if entered == PIN_CODE:
            self._ui.cat_image.show()
        else:
            def return_pin():
                self.show_pin()
                self._ui.pincode_label.setText("")

            self.hide_pin()
            self._ui.pincode_label.setText("ERROR")
            QTimer.singleShot(1000, return_pin)

    @Slot()
    def hide_pin(self):
        for btn in self.pin_digit_buttons:
            btn.hide()
        self._ui.pin_btn_enter.hide()
        self._ui.pin_btn_clr.hide()

    @Slot()
    def show_pin(self):
        for btn in self.pin_digit_buttons:
            btn.show()
        self._ui.pin_btn_enter.show()
        self._ui.pin_btn_clr.show()
