from typing import Optional

from PySide6.QtWidgets import QMainWindow, QWidget

from views.date_form import DateForm
from views.endless_loading_form import EndlessLoadingForm
from views.hello_world_form import HelloWorldForm
from views.main_window_ui import Ui_MainWindow
from views.pin_code_form import PinCodeForm
from views.hello_user_form import HelloUserForm
from views.price_form import PriceForm


class MainWindow(QMainWindow):
    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)

        self._pin_code_form = PinCodeForm()
        self._hello_world_form = HelloWorldForm()
        self._date_form = DateForm()
        self._hello_user_form = HelloUserForm()
        self._endless_loading_form = EndlessLoadingForm()
        self._price_form = PriceForm()

        self._ui.tabWidget.addTab(self._pin_code_form, "Pin Code")
        self._ui.tabWidget.addTab(self._hello_world_form, "Hello, world!")
        self._ui.tabWidget.addTab(self._date_form, "Date")
        self._ui.tabWidget.addTab(self._hello_user_form, "Hello, %username%!")
        self._ui.tabWidget.addTab(self._endless_loading_form, "Endless Loading")
        self._ui.tabWidget.addTab(self._price_form, "Price")
