import sys

from PySide6.QtWidgets import QApplication

from UI.ui import MyWidget

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    sys.exit(app.exec())
