from PyQt5.QtCore import Qt,QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont, QTextCursor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget,QVBoxLayout,QHBoxLayout,
    QLineEdit, QTextEdit,QPushButton,QFileDialog,QToolBar,QAction
)
from AppsConfiguration import AppsUI
import sys
import os
import json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import Main.main  # type:ignore
import Assets.Path_Finder.vs_path_reg as Path  # type:ignore

APP_NAME = "MyLauncher"

class CustomCLI(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("CLI")
        self.setWindowIcon(QIcon(r"Assets\Icons\terminal_icon.ico"))
        self.setFixedSize(700, 400)
        self.vscode_exe = Path.get_vscode_exe_path()
        self.git_exe=Path.get_git_exe_path()
        self.maya_exe=Path.get_maya_exe_path()
        self.command_container = []
        self.initUI()

    def initUI(self):
        self.central_wgt = QWidget()
        self.central_wgt.setStyleSheet("background-color: #B2BEB5")
        self.setCentralWidget(self.central_wgt)

        layout = QVBoxLayout(self.central_wgt)

        # Toolbar
        self.toolBar = QToolBar()
        self.toolBar.setMovable(False)
        self.toolBar.setFloatable(False)

        self.addToolBar(self.toolBar)

        open_apps_action = QAction("Apps Configuration",self)
        open_apps_action.triggered.connect(self.openAppsConfig)

        self.toolBar.addAction(open_apps_action)
        self.toolBar.setFont(QFont("Arial",10))
        self.toolBar.setStyleSheet("background-color: #B2BEB5;border-radius: 1px")


        # output
        self.output = QTextEdit()
        self.output.setReadOnly(True)
        self.output.setFont(QFont("Courier", 10))
        self.output.setStyleSheet("background-color: #1e1e1e; color: #d4d4d4; border-radius: 5px")


        # input
        self.inp_wgt=QWidget()
        self.inp_layout=QHBoxLayout(self.inp_wgt)
        self.inp_layout.setContentsMargins(0,0,0,0)
        self.input = QLineEdit()
        self.input.setPlaceholderText("<:\\>")
        self.input.setFont(QFont("Courier", 10))
        self.input.setStyleSheet("background-color: #2d2d2d; color: #ffffff; border-radius: 5px")
        self.input.returnPressed.connect(self.store_command)


        self.add_btn=QPushButton("+")
        self.add_btn.clicked.connect(self.Add_apps)
        self.add_btn.setStyleSheet("background-color: #2d2d2d; color: #ffffff; border-radius: 5px")
        self.add_btn.setFixedSize(25,25)


        self.inp_layout.addWidget(self.add_btn)
        self.inp_layout.addWidget(self.input)


        layout.addWidget(self.output)
        layout.addWidget(self.inp_wgt)

        self.command_map={
             "cmds":lambda: Main.main.cmds(),
             "cls":lambda: Main.main.cls(self.output),
             "vscode":lambda:Main.main.vscode(self.vscode_exe),
             "git": lambda:Main.main.git(self.git_exe),
             "maya":lambda:Main.main.maya(self.maya_exe),
             "github":lambda:Main.main.github()
          }

    def Add_apps(self,command=None):
        exe_path, _ = QFileDialog.getOpenFileName(
            self, "Select application", "", "Applications (*.exe *.lnk)"
        )
        if exe_path:
            name = os.path.basename(exe_path)
            data = self.load_apps()
            data["apps"].append({
                "name": name,
                "path": exe_path,
                "icon": None,
                "favorite": False,
                "command":command
            })
            self.save_apps(data)
            self.append_output(f"Added app: {name}")

    def get_config_path(self):
        base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        config_file = os.path.join(base_dir, "apps.json")
        os.makedirs(base_dir, exist_ok=True)
        return config_file

    def load_apps(self):
        path=self.get_config_path()

        if not os.path.exists(path):
            return {"apps":[]}

        try:
            with open(path,"r",encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {"apps":[]}

    def save_apps(self,data):

        path=self.get_config_path()
        tmp=path +".tmp"

        with open(tmp,"w",encoding="utf-8") as f:
            json.dump(data,f,indent=4,ensure_ascii=False)

        os.replace(tmp,path)

    def store_command(self):
          commands = self.input.text().strip()
          if commands in self.command_map:
            result=self.command_map[commands]()
            self.append_output(f">>> {result}")
            self.input.clear()
          else:
               self.append_output(f">>> Unknown Command: {commands}")
               self.input.clear()

    def append_output(self, text):
        self.output.append(text)
        self.output.moveCursor(QTextCursor.End)


    def openAppsConfig(self):
        self.openapps_window=AppsUI()
        result=self.openapps_window.exec_()
        return result

