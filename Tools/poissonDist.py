import pandas as pd
import sys, getopt
import csv

def main(argv):
    latest_year = 2018
    home = sys.argv[1]
    away = sys.argv[2]

    df = pd.read_csv('../Data/PerMinuteStats.csv')
    home_flag = df['TEAM'] == home
    away_flag = df['TEAM'] == away

    home_filtered = df[home_flag]
    away_filtered = df[away_flag]

    home_year = home_filtered['Year'] == latest_year
    away_year = away_filtered['Year'] == latest_year

    final_home_pts = home_filtered[home_year]['PTS']
    final_away_pts = away_filtered[away_year]['PTS']

    
