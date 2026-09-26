import torch  

import sys
from PyQt5.QtWidgets import QApplication
from src.gui import CredibilityApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CredibilityApp()
    window.show()
    sys.exit(app.exec_())