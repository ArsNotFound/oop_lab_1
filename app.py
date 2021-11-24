import sys

from PySide6.QtWidgets import QApplication

from views.main_window import MainWindow


class App(QApplication):
    def __init__(self, sys_argv: list[str]):
        super(App, self).__init__(sys_argv)

        self.main_window = MainWindow()
        self.main_window.show()


if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec())
