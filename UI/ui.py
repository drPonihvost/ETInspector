from PySide6 import QtCore
from PySide6.QtWidgets import QWidget, QFileDialog

from scripts.scripts import *
from .interface import Ui_Form

# pyinstaller -F -w -i "C:\Users\Philipp\Downloads\dna.ico" main.py для компиляции в exe


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.loadButton.clicked.connect(self.load)
        self.ui.clearButton.clicked.connect(self.clear)
        self.ui.exitButton.clicked.connect(self.quit_app)

    def red_script(self):
        self.ui.indentLabel.setStyleSheet(u"background-color: #DC4955;")

    def yellow_script(self):
        self.ui.indentLabel.setStyleSheet(u"background-color: #DCA555;")

    def green_script(self):
        self.ui.indentLabel.setStyleSheet(u"background-color: #7ECA8E;")

    @QtCore.Slot()
    def load(self):
        fname = QFileDialog.getOpenFileName(self, "Выбор файла", None, "File (*.txt)")[0]
        if fname:
            data = export_table_parser(fname)
            filename = data['project']['project_name']
            report = create_report(data)
            paint = {
                'invalid': self.red_script,
                'partial_valid': self.yellow_script,
                'valid': self.green_script,
            }
            paint[data['status']]()
            self.ui.indentLabel.setText(report)
            self.ui.projectNameLabel.setText(filename)
        else:
            self.clear()

    @QtCore.Slot()
    def clear(self):
        self.ui.projectNameLabel.setText('Проект не выбран')
        self.ui.indentLabel.setStyleSheet(u"background-color: rgb(232, 232, 232);")
        self.ui.indentLabel.clear()

    @QtCore.Slot()
    def quit_app(self):
        self.close()
