from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont, QTextCursor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QLineEdit, QTextEdit
)
import sys

class CustomCLI(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("CLI")
        self.setWindowIcon(QIcon(r"Assets\terminal_icon.ico"))
        self.setFixedSize(600, 300)
        self.command_container = []
        self.initUI()

    def initUI(self):
        self.central_wgt = QWidget()
        self.setCentralWidget(self.central_wgt)

        layout = QVBoxLayout(self.central_wgt)

        self.output = QTextEdit()
        self.output.setReadOnly(True)
        self.output.setFont(QFont("Courier", 10))
        self.output.setStyleSheet("background-color: #1e1e1e; color: #d4d4d4;")

        self.input = QLineEdit()
        self.input.setPlaceholderText("<:\\>")
        self.input.setFont(QFont("Courier", 10))
        self.input.setStyleSheet("background-color: #2d2d2d; color: #ffffff;")
        self.input.returnPressed.connect(self.store_command)

        layout.addWidget(self.output)
        layout.addWidget(self.input)

    def store_command(self):
        command = self.input.text().strip()
        if command:
            self.command_container.append(command)
            self.append_output(f"<:\\> {command}")
            self.input.clear()

    def append_output(self, text):
        self.output.append(text)
        self.output.moveCursor(QTextCursor.End)
        
    def keyPressEvent(self, event):
          if event.key() == Qt.Key_Up and self.command_container:
                    self.input.setText(self.command_container[-1])
 
def main():
    app = QApplication(sys.argv)
    window = CustomCLI()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
