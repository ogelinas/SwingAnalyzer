from pandas import json_normalize

import json
import numpy as np
import pandas as pd


# File to load
sim_file = 'Golf-SIM_SESSION.json'
club_file = 'Golf-CLUB.json'
club_types_file = 'Golf-CLUB_TYPES.json'


def load_json(filename):
    # Load Simulations
    with open(filename, "r") as file:
        data = json.load(file)['data']

    return json_normalize(data)


def df_simulations():
    return load_json(sim_file)


def df_clubs():
    return load_json(club_file)


def df_club_types():
    return load_json(club_types_file)


def df_bag():
    clubs = df_clubs()
    club_types = df_club_types()
    return pd.merge(clubs, club_types, left_on='clubTypeId', right_on='value')


def format_datas(df):
    # Converting shotTime to Date
    df['shotTime'] = pd.to_datetime(df['shotTime']).dt.tz_convert('America/Toronto')
    # df['shotTime'] = df['shotTime'].tz_localize('US/Eastern')
    df['date'] = df['shotTime'].dt.date
    df['date_y_m_d'] = df['shotTime'].dt.strftime("%Y-%m-%d")
    df['date_y_m_w'] = df['shotTime'].dt.strftime("%Y-%m-%W")
    df['date_y_m'] = df['shotTime'].dt.strftime("%Y-%m")
    df['date_y'] = df['shotTime'].dt.strftime("%Y")

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

    return df


def df_shots():
    data = df_simulations()
    bag = df_bag()

    # Explode Shots from All Simulations
    shots = data.explode(column='shots', ignore_index=True)
    shots = json_normalize(shots)
    shots = data['shots'].explode().pipe(lambda x: json_normalize(x).set_index(x.index))
    
    shots = pd.merge(shots, bag, left_on='clubId', right_on='id')
    shots = format_datas(shots)
    return shots