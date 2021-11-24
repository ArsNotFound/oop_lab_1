from typing import Optional

from PySide6.QtCore import Slot, Qt
from PySide6.QtWidgets import QWidget

from views.hello_world_form_ui import Ui_HelloWorldForm

HELLO_WORLD_TEXT = {
    "English": "Hello, world!",
    "Русский": "Привет, мир!",
    "Español": "¡Hola Mundo!",
    "Deutsch": "Hallo Welt!",
    "Français": "Bonjour le monde!",
}


class HelloWorldForm(QWidget):
    def __init__(self, parent: Optional[QWidget] = None):
        super(HelloWorldForm, self).__init__(parent)
        self._ui = Ui_HelloWorldForm()
        self._ui.setupUi(self)

        self.hello_straight_text = True

        for (k, _) in HELLO_WORLD_TEXT.items():
            self._ui.language_comboBox.addItem(k)

        self._ui.language_comboBox.currentTextChanged.connect(self.hello_on_language_change)
        self._ui.language_comboBox.setCurrentIndex(0)

        self._ui.hello_label.setText(HELLO_WORLD_TEXT["English"])

        self._ui.bold_checkBox.stateChanged.connect(self.hello_on_font_change)
        self._ui.italic_checkBox.stateChanged.connect(self.hello_on_font_change)
        self._ui.underline_checkBox.stateChanged.connect(self.hello_on_font_change)

        self._ui.fontSize_label.setText(str(self._ui.fontSize_slideBar.value()))
        self._ui.fontSize_slideBar.valueChanged.connect(self.hello_on_font_change)

        self._ui.font_ComboBox.setCurrentFont("Arial")
        self._ui.font_ComboBox.currentFontChanged.connect(self.hello_on_font_change)

        self._ui.straight_radioButton.setChecked(True)
        self._ui.straight_radioButton.toggled.connect(self.hello_on_letter_order_change)
        self._ui.reversed_radioButton.toggled.connect(self.hello_on_letter_order_change)

    @Slot()
    def hello_on_language_change(self):
        lang = self._ui.language_comboBox.currentText()
        text = HELLO_WORLD_TEXT.get(lang, "Something went wrong")
        text = text if self.hello_straight_text else text[::-1]
        self._ui.hello_label.setText(text)

    @Slot()
    def hello_on_font_change(self):
        sender = self.sender()
        font = self._ui.hello_label.font()

        match sender:
            case self._ui.bold_checkBox:
                font.setBold(self._ui.bold_checkBox.checkState() == Qt.CheckState.Checked)
            case self._ui.italic_checkBox:
                font.setItalic(self._ui.italic_checkBox.checkState() == Qt.CheckState.Checked)
            case self._ui.underline_checkBox:
                font.setUnderline(self._ui.underline_checkBox.checkState() == Qt.CheckState.Checked)
            case self._ui.fontSize_slideBar:
                value = self._ui.fontSize_slideBar.value()
                font.setPointSize(value)
                self._ui.fontSize_label.setText(str(value))
            case self._ui.font_ComboBox:
                font.setFamily(self._ui.font_ComboBox.currentFont().family())

        self._ui.hello_label.setFont(font)

    @Slot()
    def hello_on_letter_order_change(self):
        sender = self.sender()
        match sender:
            case self._ui.straight_radioButton:
                if self._ui.straight_radioButton.isChecked():
                    if not self.hello_straight_text:
                        self.hello_straight_text = True
                        self._ui.hello_label.setText(self._ui.hello_label.text()[::-1])

            case self._ui.reversed_radioButton:
                if self._ui.reversed_radioButton.isChecked():
                    if self.hello_straight_text:
                        self.hello_straight_text = False
                        self._ui.hello_label.setText(self._ui.hello_label.text()[::-1])
