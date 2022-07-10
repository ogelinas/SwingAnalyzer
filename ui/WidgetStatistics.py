# Imports
from matplotlib.axis import Axis
from matplotlib.axes import Axes
from pandas import DataFrame

from utilities.Club import Club
from utilities.Metric import Metric
from utilities.GroupBy import GroupBy

from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT

from PyQt6.QtCore import Qt, Slot
from PyQt6.QtWidgets import (
    QWidget,
    QDoubleSpinBox,
    QVBoxLayout,
    QHBoxLayout,
)

import numpy as np
# from scipy.stats import norm


class WidgetStatistics(QWidget):
    def __init__(self, df: DataFrame, club: Club=None, n_last=5, parent=None):
        super().__init__(parent)

        self.club = club
        # self.club = Club.DRIVER

        self.n_last = n_last
        
        self.df = df

        #  create widgets
        # self.view = FigureCanvas(Figure(figsize=(5, 3)))
        self.view = FigureCanvas(Figure())

        # self.setStyleSheet("background-color:blue;")

        # self.view.style.use('dark_background')
        # self.style.use('dark_background')
        # self.view.plt.style.use('dark_background')

        # self.axes = self.view.figure.subplots()
        self.axes: Axes = self.view.figure.subplots(nrows=2, ncols=4)
        self.view.figure.subplots_adjust(wspace=0.3, hspace=0.3)
        self.toolbar = NavigationToolbar2QT(self.view, self)
        # self.mu_input = QDoubleSpinBox()
        # self.std_input = QDoubleSpinBox()
        # self.mu_input.setPrefix("μ: ")
        # self.std_input.setPrefix("σ: ")
        # self.std_input.setValue(10)

        #  Create layout
        # input_layout = QHBoxLayout()
        # input_layout.addWidget(self.mu_input)
        # input_layout.addWidget(self.std_input)
        vlayout = QVBoxLayout()
        vlayout.addWidget(self.toolbar)
        vlayout.addWidget(self.view)
        #vlayout.addLayout(input_layout)
        self.setLayout(vlayout)

        # connect inputs with on_change method
        # self.mu_input.valueChanged.connect(self.on_change)
        # self.std_input.valueChanged.connect(self.on_change)

        self.on_change()

    @Slot()
    def on_change(self):
        """ Update the plot with the current input values """
        # mu = self.mu_input.value()
        # std = self.std_input.value()

        

        # x = np.linspace(-100, 100)
        # y = norm.pdf(x, mu, std)
        # y = range(0, len(x))

        # self.axes.clear()
        # self.axes[0,0].plot(x, y)

        axs = self.axes
        club = self.club
        n_last = self.n_last

        if club:
            self.view.figure.suptitle(club.text, fontsize=14, fontweight='bold')
            print(club.text)

            df=self.df[self.df.name == club.text]
            # df=self.df

            # self.axes[0,0] = plot(df=df, ax=axs[0,0], metric=Metric.CARRY_DISTANCE)
            plot(df=df, ax=axs[0,0], n_last=n_last, metric=Metric.CARRY_DISTANCE)
            plot(df=df, ax=axs[1,0], n_last=n_last, metric=Metric.CLUB_HEAD_SPEED)

            plot(df=df, ax=axs[0,1], n_last=n_last, metric=Metric.BACK_SPIN)
            plot(df=df, ax=axs[1,1], n_last=n_last, metric=Metric.ATTACK_ANGLE)

            plot(df=df, ax=axs[0,2], n_last=n_last, metric=Metric.CARRY_DEVIATION_DISTANCE)
            plot(df=df, ax=axs[1,2], n_last=n_last, metric=Metric.VERTICAL_LAUNCH_ANGLE)

            plot(df=df, ax=axs[0,3], n_last=n_last, metric=Metric.SIDE_SPIN)
            plot(df=df, ax=axs[1,3], n_last=n_last, metric=Metric.CLUB_PATH_ANGLE)

        # self.axes.cla()

        self.view.draw()
        
        print("draw()")





def plot(df: DataFrame, n_last ,ax: Axis, metric: Metric):

    # df_grouped = df.groupby("date")[metric.data]
    # df_grouped = df.groupby(["date"])
    df_grouped = df.groupby(["date"])
    # df_grouped = df_grouped.head(1)
    df_grouped = df_grouped[metric.data]

    data = []
    dates = list(df_grouped.groups)
    for group_date in dates[-n_last:] if len(dates) > n_last else dates:
        data.append(df_grouped.get_group(group_date))

    if len(data) > 0:

        labels = []
        labels.extend(range(1, len(data) + 1))
        labels.reverse()


        ax.boxplot(
            x=data,
            # labels=list(df_grouped.groups),
            # labels=list([i for i in range[0,len(data)]]),
            labels=labels,
            meanline=True,
            showmeans=True,
            showfliers=False,
            notch=False,
            vert=metric.vert
        )

        series_label = 'Session'
        ax.set_title(metric.short_description)
        if metric.vert:
            ax.set_xlabel(series_label)
            ax.set_ylabel(metric.long_description)
        else:
            ax.set_xlabel(metric.long_description)
            ax.set_ylabel(series_label)

        ax.grid()

    return ax