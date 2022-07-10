from PyQt6.QtWidgets import QWidget, QHBoxLayout, QDoubleSpinBox, QLabel


class DoubleSpinBox(QDoubleSpinBox):

    def __init__(self) -> None:
        super().__init__()
        self.setMinimum(1)
        self.setMaximum(12)
        self.setDecimals(0)
        self.lineEdit().setReadOnly(True)
        self.lineEdit().setEnabled(True)

class WidgetLast(QWidget):

    def __init__(self) -> None:
        super().__init__()

        layout = QHBoxLayout(self)

        self.double_spin_box = DoubleSpinBox()

        label = QLabel(self)
        label.setText("Last n:")
        label.setBuddy(self.double_spin_box)
        
        layout.addWidget(label)
        layout.addWidget(self.double_spin_box)

        self.setLayout(layout)

    @property
    def n(self) -> int:
        return int(self.double_spin_box.value())

    @n.setter
    def n(self, n):
        self.double_spin_box.setValue(n)