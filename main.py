from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys


class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Hello Title")
        self.setGeometry(300, 250, 350, 200)

        self.new_text = QtWidgets.QLabel(self)
        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText("Main Label")
        self.main_text.move(100, 100)
        self.main_text.adjustSize()

        self.btn = QtWidgets.QPushButton(self)
        self.btn.move(70, 150)
        self.btn.setText("Click Me")
        self.btn.setFixedWidth(200)
        self.btn.clicked.connect(self.add_label)

    def add_label(self):
        if self.new_text.hide():
            self.new_text.setText("New Label by click")
            self.new_text.move(100, 50)
            self.new_text.adjustSize()
        else:
            self.new_text.hide()

def application():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
