from PyQt5.QtWidgets import QApplication
import sys
from UI import CustomCLI

def main():
    app = QApplication(sys.argv)
    window = CustomCLI()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
