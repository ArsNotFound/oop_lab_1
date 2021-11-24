import datetime
from typing import Optional

from PySide6.QtCore import QDate, Slot
from PySide6.QtWidgets import QWidget

from views.date_form_ui import Ui_DateForm


class DateForm(QWidget):
    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)
        self._ui = Ui_DateForm()
        self._ui.setupUi(self)

        self._ui.calendar.selectionChanged.connect(self.date_changed)
        self._ui.calendar.setSelectedDate(QDate.currentDate())

    @Slot()
    def date_changed(self):
        selected_date: QDate = self._ui.calendar.selectedDate()
        date = datetime.date(selected_date.year(), selected_date.month(), selected_date.day())
        current_date = date.today()
        delta = current_date - date

        if delta != abs(delta):
            self._ui.day_passed_label.setText(f"До выбранного дня осталось: {abs(delta.days)} дней")
        else:
            self._ui.day_passed_label.setText(f"С выбранного дня прошло: {abs(delta.days)} дней")
