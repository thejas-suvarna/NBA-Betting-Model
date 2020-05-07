from bs4 import BeautifulSoup
import requests
import lxml
import os
import sys

import pandas as pd


def try_concat(x, y):
    try:
        return str(x) + str(y)[0:4]
    except (ValueError, TypeError):
        return np.nan


# os.path.join(sys.path[0], "nba odds 2007-2020.xlsx")
df = pd.concat(pd.read_excel(os.path.join(sys.path[0], "nba odds 2007-2020.xlsx"), sheet_name=None), ignore_index=True)
# id = str(str(df['Full_Date']) + df["Team"][0:4])
# df["id"] = id
# df["id"] = df.Full_Date.map(str) + df.Team[0:4]
df['id'] = [try_concat(x, y) for x, y in zip(df['Full_Date'], df['Team'])]
is_V = df['VH'] == 'V'
df_V = df[is_V]
is_H = df['VH'] == 'H'
df_H = df[is_H]
df_V1 = df_V.rename(columns={'Date': 'Date1', 'Rot': 'Rot1',
                             'VH': 'VH1', 'Team': 'Team1', '1st': '1st1', '2nd': '2nd1',
                             '3rd': '3rd1', '4th': '4th1', 'Final': 'Final1', 'Open': 'Open1',
                             'Close': 'Close1', 'ML': 'ML1', '2H': '2H1', 'Year': 'Year1',
                             'Full_Date': 'Full_Date1', 'id': 'id1'})
df_H2 = df_H.rename(columns={'Date': 'Date2', 'Rot': 'Rot2',
                             'VH': 'VH2', 'Team': 'Team2', '1st': '1st2', '2nd': '2nd2',
                             '3rd': '3rd2', '4th': '4th2', 'Final': 'Final2', 'Open': 'Open2',
                             'Close': 'Close2', 'ML': 'ML2', '2H': '2H2', 'Year': 'Year2',
                             'Full_Date': 'Full_Date2', 'id': 'id2'})
df_V1 = df_V1.reset_index(drop=True)
df_H2 = df_H2.reset_index(drop=True)
df_horizontal = pd.concat([df_V1, df_H2], axis=1)
pd.set_option('display.max_columns', 40)
# print(df)
print(df_horizontal)
