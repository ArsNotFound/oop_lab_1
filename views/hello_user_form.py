from typing import Optional

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QWidget

from views.hello_user_form_ui import Ui_HelloUserForm


class HelloUserForm(QWidget):
    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)
        self._ui = Ui_HelloUserForm()
        self._ui.setupUi(self)

        self._ui.name_lineEdit.textChanged.connect(self.hello_user_change)

    @Slot()
    def hello_user_change(self):
        name = self._ui.name_lineEdit.text().strip()
        if name == "":
            name = "%username%"

        self._ui.helloUser_label.setText(f"Hello, {name}")
