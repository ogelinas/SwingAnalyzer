from PyQt6.QtWidgets import QWidget, QMainWindow, QHBoxLayout, QVBoxLayout

from PyQt6.QtWidgets import QSplitter
from PyQt6.QtCore import Qt

from PyQt6 import QtGui
from matplotlib import widgets

from ui.MenuBar import MenuBar
from ui.StatusBar import StatusBar
from ui.WidgetClubs import WidgetClubs
from ui.WidgetGroupBy import WidgetGroubBy
from ui.WidgetLast import WidgetLast

from ui.WidgetStatistics import WidgetStatistics
from utilities.GroupBy import GroupBy

from utilities.LoadData import df_shots

from utilities.Club import Club

import sys


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setMenuBar(MenuBar())
        self.setWindowTitle("Swing Analyzer")

        self.shots = df_shots()

        self.setStatusBar(StatusBar())

        self.splitter = QSplitter(Qt.Orientation.Horizontal)

        # Data
        # Golf Clubs
        widget_data_selection = QWidget()
        width = 175
        widget_data_selection.setMinimumWidth(width)
        widget_data_selection.setMaximumWidth(width)

        data_selection_layout = QVBoxLayout()
        widget_data_selection.setLayout(data_selection_layout)

        self.widget_group_by = WidgetGroubBy()
        data_selection_layout.addWidget(self.widget_group_by)

        self.widget_last = WidgetLast()
        data_selection_layout.addWidget(self.widget_last)
        self.widget_last.n = 5
        # self.widget_last.com valueChanged.connect(self.replace_widget)
        self.widget_last.double_spin_box.valueChanged.connect(self.replace_widget)

        self.widget_clubs = WidgetClubs()
        self.widget_clubs.currentItemChanged.connect(self.club_changed)
        # self.widget_clubs.selectionModel().selectionChanged.connect(self.club_change)
        data_selection_layout.addWidget(self.widget_clubs)

        self.splitter.addWidget(widget_data_selection)

        # Statistics
        self.splitter.addWidget(QWidget())
        self.widget_shots = None

        layout = QHBoxLayout(self)
        layout.addWidget(self.splitter)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.showMaximized()


    def club_changed(self, item): # Not an index, i is a QListItem
        # club:Club = item.data(Qt.ItemDataRole.UserRole)
        # print(f"index_changed(type(i.data)): {club.text}")
        # widget_shots = WidgetStatistics(df=self.shots, club=club)
        # self.splitter.replaceWidget(1, widget_shots)
        self.replace_widget()

    def replace_widget(self):
        list_widget_item = self.widget_clubs.selectedItems()

        # print([item.text() for item in self.widget_clubs.selectedItems()])

        # club = self.widget_clubs.club_selected

        # print(club)

        if len(list_widget_item) == 1:
            # club = list_widget_item[0].data(Qt.ItemDataRole.UserRole)

            club = self.widget_clubs.club

            # group_by = self.widget_group_by

            # club = self.widget_clubs.club_selected

            print(f"club: {club}")

            n_last = self.widget_last.n
            print(f"last n: {n_last}")

            widget_shots = WidgetStatistics(df=self.shots, club=club, n_last=n_last)
            self.splitter.replaceWidget(1, widget_shots)

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        # return super().closeEvent(event)
        event.accept()
        sys.exit()
        
        
