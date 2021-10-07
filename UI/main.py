import sys

from PySide6 import QtCore
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog

from interface import Ui_Form


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.loadButton.clicked.connect(self.load)
        self.ui.clearButton.clicked.connect(self.clear)
        self.ui.exitButton.clicked.connect(self.quit_app)

    def load(self):
        fname = QFileDialog.getOpenFileName(self, "Выбор файла", None, "File (*.txt)")[0]
        self.ui.projectNameLabel.setText(f'{fname}')
        if fname:
            f = open(fname, 'r')
            self.ui.indentLabel.setText(f.read())
        else:
            self.clear()

    def clear(self):
        self.ui.projectNameLabel.setText('Проект не выбран')
        self.ui.indentLabel.clear()

    @QtCore.Slot()
    def quit_app(self):
        app.quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    sys.exit(app.exec())
