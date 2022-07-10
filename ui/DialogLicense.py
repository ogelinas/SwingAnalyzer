from PyQt6.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QLabel, QPlainTextEdit

from PyQt6.QtCore import Qt


class DialogLicense(QDialog):

    def __init__(self):
        super().__init__()

        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setWindowTitle("About")

        self.setLayout(QVBoxLayout())

        label = QLabel()
        label.setText("Swing Analyzer")
        self.layout().addWidget(label)

        license = QPlainTextEdit()
        license.setMinimumWidth(480)
        license.setMinimumHeight(500)
        license.setReadOnly(True)

        with open("LICENSE", "r") as file:
            text = file.read()
            license.textCursor().insertText(text)

        self.layout().addWidget(license)
        
        dialogButtons = QDialogButtonBox(self)
        dialogButtons.setStandardButtons(QDialogButtonBox.StandardButton.Ok)
        dialogButtons.accepted.connect(self.accept)

        self.layout().addWidget(dialogButtons)

        self.exec()
