from PyQt6.QtWidgets import QMenuBar, QApplication
from PyQt6.QtGui import QIcon, QAction

from ui.DialogLicense import DialogLicense


class MenuBar(QMenuBar):

    def __init__(self):
        super().__init__()

        
        file_menu = self.addMenu("&File")

        button_exit = QAction("&Exit", self)
        button_exit.setStatusTip("Exit application")
        button_exit.triggered.connect(QApplication.instance().quit)
        button_exit.setShortcut('Ctrl+Q')
        file_menu.addAction(button_exit)


        help_menu = self.addMenu("&Help")

        button_about = QAction("&About", self)
        button_about.setStatusTip("About")
        button_about.triggered.connect(DialogLicense)
        help_menu.addAction(button_about)


