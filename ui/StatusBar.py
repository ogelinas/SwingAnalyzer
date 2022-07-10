from PyQt6.QtWidgets import QStatusBar


class StatusBar(QStatusBar):

    def __init__(self) -> None:
        super().__init__()

        self.showMessage("")