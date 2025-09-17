from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont, QTextCursor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QLineEdit, QTextEdit
)
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import Main.main
import Assets.Path_Finder.vs_path_reg as Path

class CustomCLI(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("CLI")
        self.setWindowIcon(QIcon(r"Assets\Icons\terminal_icon.ico"))
        self.setFixedSize(600, 300)
        self.vscode_exe = Path.get_vscode_exe_path()
        self.git_exe=Path.get_git_exe_path()
        self.maya_exe=Path.get_maya_exe_path()
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
        self.command_map={
             "sayhello":Main.main.sayhello,
             "cls":lambda: Main.main.cls(self.output),
             "vscode":lambda:Main.main.vscode(self.vscode_exe),
             "git": lambda:Main.main.git(self.git_exe),
             "maya":lambda:Main.main.maya(self.maya_exe)
          }

    def store_command(self):
          command = self.input.text().strip()
          if command in self.command_map:
            result=self.command_map[command]()
            self.append_output(f">>> {result}")
            self.input.clear()
          else:
               self.append_output(">>> Unknown Command")
               self.input.clear()

    def append_output(self, text):
        self.output.append(text)
        self.output.moveCursor(QTextCursor.End)
 
def main():
    app = QApplication(sys.argv)
    window = CustomCLI()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
