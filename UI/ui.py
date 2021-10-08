from PySide6 import QtCore
from PySide6.QtWidgets import QWidget, QFileDialog

from .interface import Ui_Form
from scripts.scripts import *


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.loadButton.clicked.connect(self.load)
        self.ui.clearButton.clicked.connect(self.clear)
        self.ui.exitButton.clicked.connect(self.quit_app)

    @QtCore.Slot()
    def load(self):
        fname = QFileDialog.getOpenFileName(self, "Выбор файла", None, "File (*.txt)")[0]
        if fname:
            data = parser(fname)
            filename = [name for name in data['project']][0]
            self.ui.indentLabel.setText(create_report(data))
            self.ui.projectNameLabel.setText(filename)
        else:
            self.clear()

    @QtCore.Slot()
    def clear(self):
        self.ui.projectNameLabel.setText('Проект не выбран')
        self.ui.indentLabel.clear()

    @QtCore.Slot()
    def quit_app(self):
        self.close()



