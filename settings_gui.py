import settings_design

from PyQt5 import QtWidgets


class SettingsApp(QtWidgets.QMainWindow, settings_design.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)