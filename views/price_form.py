from typing import Optional

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QWidget

from views.price_form_ui import Ui_PriceForm


class PriceForm(QWidget):
    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)
        self.ui = Ui_PriceForm()
        self.ui.setupUi(self)

        self.ui.price_spinBox.valueChanged.connect(self.price_on_value_change)
        self.ui.count_spinBox.valueChanged.connect(self.price_on_value_change)
        self.ui.price_spinBox.setValue(0)
        self.ui.count_spinBox.setValue(0)

    @Slot()
    def price_on_value_change(self):
        total = self.ui.price_spinBox.value() * self.ui.count_spinBox.value()
        self.ui.total_lineEdit.setText(str(total))
