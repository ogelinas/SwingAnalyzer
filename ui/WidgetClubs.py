from PyQt6.QtWidgets import QListWidget, QListWidgetItem
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon

from utilities.Club import Club


class WidgetClubs(QListWidget):

    def __init__(self):
        super().__init__()

        self.club = None

        for club in Club:
            list_item = QListWidgetItem(club.text)
            list_item.setIcon(QIcon(f"img/{club.familly}.png"))
            list_item.setData(Qt.ItemDataRole.UserRole, club)
            self.addItem(list_item)
            ## self. s ..valueChanged.connect(self.on_change)
            # self.selectionChanged.changeEvent.connect(self.on_change)
            self.currentItemChanged.connect(self.on_changed)

    def on_changed(self, item): # Not an index, i is a QListItem
        self.club = item.data(Qt.ItemDataRole.UserRole)
