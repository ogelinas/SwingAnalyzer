from PyQt6.QtWidgets import QWidget, QHBoxLayout, QComboBox, QLabel
from utilities.GroupBy import GroupBy


class ComboBox(QComboBox):

    def __init__(self) -> None:
        super().__init__()

        for group_by in GroupBy:
            self.addItem(group_by.periode, userData=group_by)


class WidgetGroubBy(QWidget):

    def __init__(self) -> None:
        super().__init__()

        layout = QHBoxLayout(self)

        self.combobox = ComboBox()

        label = QLabel(self)
        label.setText("Group By:")
        label.setBuddy(self.combobox)
        
        layout.addWidget(label)
        layout.addWidget(self.combobox)

        self.setLayout(layout)