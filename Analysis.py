import pandas as pd
import json
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.axes import Axes
from matplotlib.axis import Axis

from pandas import json_normalize, DataFrame

from utilities.Club import Club
from utilities.Metric import Metric


club = Club.DRIVER

# File to load
sim_file = 'Golf-SIM_SESSION.json'
club_file = 'Golf-CLUB.json'
club_types_file = 'Golf-CLUB_TYPES.json'

# Load Simulations
with open(sim_file, "r") as file:
    sim_json = json.load(file)['data']

sim_data = json_normalize(sim_json)

# Explode Shots from All Simulations
shots = sim_data.explode(column='shots', ignore_index=True)
shots = json_normalize(shots)
shots = sim_data['shots'].explode().pipe(lambda x: pd.json_normalize(x).set_index(x.index))

# Load Clubs
club_json = pd.read_json(club_file)['data']
clubdata = pd.DataFrame.from_dict(json_normalize(club_json))

# Load Club Types
clubtype_json = pd.read_json(club_types_file)['data']
clubtypedata = pd.DataFrame.from_dict(json_normalize(clubtype_json))

# Create Bag from Club and Club Type
bag = pd.merge(clubdata, clubtypedata, left_on='clubTypeId', right_on='value')

# Create the DataFrame
df = pd.merge(shots, bag, left_on='clubId', right_on='id')

# Converting shotTime to Date
df['shotTime'] = pd.to_datetime(df['shotTime'])
df['date'] = df['shotTime'].dt.date

# Converting Distance Meter to Yard
convert_m_to_yd = 1.093613298
df['carryDistance'] = df['carryDistance'].apply(lambda x: x * convert_m_to_yd)
df['carryDeviationDistance'] = df['carryDeviationDistance'].apply(lambda x: x * convert_m_to_yd)

# Converting Distance Yard to Feet
# convert_yd_to_m = 3
# df['apexHeight'] = df['apexHeight'].apply(lambda x: x * convert_yd_to_m)

# Converting Speed from m/s to mil/hr
convert_m_per_s_to_mil_per_hr = 2.236936292
df['clubHeadSpeed'] = df['clubHeadSpeed'].apply(lambda x: x * convert_m_per_s_to_mil_per_hr)
df['ballSpeed'] = df['ballSpeed'].apply(lambda x: x * convert_m_per_s_to_mil_per_hr)

# Adding Golf Metric
df['backSpin'] = df['spinRate'] * np.cos(np.deg2rad(df['spinAxis']))
df['sideSpin'] = df['spinRate'] * -1 * np.sin(np.deg2rad(df['spinAxis']))
df['smashFactor'] = df['ballSpeed'] / df['clubHeadSpeed']
df['tempo'] = df['backSwingTime'] / df['downSwingTime']


# Filter by club name
df = df[df.name == club.value]


# Plot
fig, axs = plt.subplots(nrows=2, ncols=4)
fig.suptitle(club.value, fontsize=14, fontweight='bold')

def plot(df: DataFrame, ax: Axis, metric: Metric):

    n_last = 4

    # df_grouped = df.groupby("date")[metric.data]
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


plot(df=df, ax=axs[0,0], metric=Metric.CARRY_DISTANCE)
plot(df=df, ax=axs[1,0], metric=Metric.CLUB_HEAD_SPEED)

plot(df=df, ax=axs[0,1], metric=Metric.BACK_SPIN)
plot(df=df, ax=axs[1,1], metric=Metric.ATTACK_ANGLE)

plot(df=df, ax=axs[0,2], metric=Metric.TEMPO)
plot(df=df, ax=axs[1,2], metric=Metric.VERTICAL_LAUNCH_ANGLE)

plot(df=df, ax=axs[0,3], metric=Metric.SIDE_SPIN)
plot(df=df, ax=axs[1,3], metric=Metric.CLUB_PATH_ANGLE)

plt.show()