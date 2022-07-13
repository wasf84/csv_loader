# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication
from app_csvloader import App_csvloader

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = App_csvloader()
    win.show()
    sys.exit(app.exec())
