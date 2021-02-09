import sys
from PyQt5.QtWidgets import (QWidget, QApplication,
                             QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QLineEdit)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.counter = 0

    def init_ui(self):
        self.text_label = QLabel("There has been no name entered; so, I cannot do anything yet!")
        self.label = QLabel("Name: ")
        self.name_input = QLineEdit()
        self.button = QPushButton("Clicked: 0")

        self.button.setText("Set Name")
        self.button.clicked.connect(self.alterName)

        h = QHBoxLayout()
        h.addWidget(self.label)
        h.addWidget(self.name_input)

        v = QVBoxLayout()

        v.addWidget(self.text_label)
        v.addLayout(h)
        v.addWidget(self.button)

        self.setLayout(v)

        self.setWindowTitle("Nothing has been clicked!")
        self.show()

    def alterName(self):
        inputted_text = self.name_input.text()
        Our_string = "You have entered " + "'" + inputted_text + "'"
        self.text_label.setText(Our_string)
        self.setWindowTitle(inputted_text + "'s Window")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())



