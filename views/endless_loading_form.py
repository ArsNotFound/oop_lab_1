from typing import Optional

from PySide6.QtCore import Slot, QTimer
from PySide6.QtWidgets import QWidget

from views.endless_loading_form_ui import Ui_EndlessLoadingForm


class EndlessLoadingForm(QWidget):
    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)
        self._ui = Ui_EndlessLoadingForm()
        self._ui.setupUi(self)

        self._ui.start_progress_bar_btn.pressed.connect(self.endless_loading_start)

    @Slot()
    def endless_loading_start(self):
        self._ui.endless_progressBar.setValue(80)
        QTimer.singleShot(60 * 1000, lambda: self._ui.endless_progressBar.setValue(100))
