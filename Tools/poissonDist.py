import pandas as pd
import sys, getopt
import numpy

# When passing in command line arguments, must have in the format of 'Golden State Warriors' to ignore whitespace

def main(argv):
    game_minutes = 48
    latest_year = 2018
    home = sys.argv[1]
    away = sys.argv[2]

    df = pd.read_csv("../Data/PerMinuteStats.csv")
    home_flag = df['TEAM'] == home
    away_flag = df['TEAM'] == away

    home_filtered = df[home_flag]
    away_filtered = df[away_flag]

    home_year = home_filtered['Year'] == latest_year
    away_year = away_filtered['Year'] == latest_year

    final_home_pts = home_filtered[home_year]['PTS'] * game_minutes
    final_away_pts = away_filtered[away_year]['PTS'] * game_minutes

    home_dist = numpy.random.poisson(final_home_pts, 10000)
    away_dist = numpy.random.poisson(final_away_pts, 10000)

    scorelines = {}

    for x in range(0, 9999):
        score = (home_dist[x], away_dist[x])
        if score in scorelines.keys():
            scorelines[score] += 1
        else:
            scorelines[score] = 1
    max = 0
    result = (-1, -1)

    for score in scorelines:
        if scorelines[score] > max:
            max = scorelines[score]
            result = score

    print(result)

if __name__ == "__main__":
    main(sys.argv[1:])
