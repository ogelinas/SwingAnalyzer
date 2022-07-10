import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget

from ui.MainWindow import MainWindow


class SwingAnalyzer(QWidget):

    def __init__(self):
        super().__init__()
        # self.setWindowTitle("Swing Analyzer")
        self.main_window = MainWindow()


def main():

    app = QApplication(sys.argv)
    swing_analyzer = SwingAnalyzer()
    swing_analyzer.main_window.show()

    with open("ui/style.qss", "r") as file:
        style = file.read()
        app.setStyleSheet(style)

    sys.exit(app.exec())


if __name__ == "__main__":
    main()