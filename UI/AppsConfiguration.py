from PyQt5.QtCore import Qt,QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont, QTextCursor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget,QDialog,QLabel,
    QVBoxLayout,QHBoxLayout, QLineEdit, QTextEdit,QPushButton,QFileDialog
)
import sys
import os
import json


class AppsUI(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("Apps Configuration")
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.setFixedSize(300,300)
        self.UI()
    def UI(self):
        self.setStyleSheet("background-color: #B2BEB5")
        self.layout=QVBoxLayout(self)

        apps_wgt=self.app_data_loader()
        self.layout.addWidget(apps_wgt)


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


    def app_data_loader(self):
        data=self.load_apps()

        data_wgt=QWidget()
        layout=QVBoxLayout(data_wgt)

        for app in data["apps"]:
            Hwgt=QWidget()
            Hlayout=QHBoxLayout(Hwgt)
            app_name=QLabel(app["name"])

            app_path=QLabel(app["path"])
            Hlayout.addWidget(app_name)
            Hlayout.setSpacing(2)
            Hlayout.addWidget(app_path)
            layout.addWidget(Hwgt)
        return data_wgt

