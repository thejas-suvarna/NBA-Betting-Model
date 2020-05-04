#These are the packages that you will need to install in your environment
#Create a folder. Run 'python3 -m venv venv'#Create a folder. Run 'python -m venv venv' (for non python3.x)#Run 'source venv/bin/activate' <- you are now in the virtual environment#Run 'venv/scripts/activate.bat' for windows#install packages using pip
#run this file using "python ZipScraper.py"
from bs4 import BeautifulSoup
import requests
import helper
import csv
# import usaddress
# import helper
import json
import pandas as pd

data_array = []

for year in range(1999, 2021):
    print(year)
    playoffs = 0
    #Build URL LIST
    year_url = "https://www.basketball-reference.com/leagues/NBA_" + str(year) + "_games.html"
    response = requests.get(year_url, timeout=120)
    content = BeautifulSoup(response.content, "html.parser")
    months = content.find('div', attrs={"class": "filter"})
    url_list = []
    for month in months.findAll('a'):
        url_list.append("https://www.basketball-reference.com" + month["href"])
        # print(url_list)

    #Get Data
    for month_url in url_list:
        # print(month_url)
        response1 = requests.get(month_url, timeout=120)
        content1 = BeautifulSoup(response1.content, "html.parser")
        games = content1.find('tbody')
        for game in games.findAll('tr'):
            game_array = []
            for item in game.contents:
                game_array.append(item.text)
            try:
                day, game_array[0] = helper.date_fix(game_array[0])
                id = game_array[0] + game_array[2].replace(" ", "")[0:4]
                data_array.append([id, game_array[0], day, game_array[2], game_array[3], game_array[4], game_array[5], playoffs])
            except:
                # print("error")
                playoffs = 1
                            # ["id", "Date", "Day", "Home Team", "Home Score", "Away Team", "Away Score", "Playoffs"]
            

df = pd.DataFrame(data = data_array, columns = ["id", "Date", "Day", "Home Team", "Home Score", "Away Team", "Away Score", "Playoffs"] )
print(df)

df.to_csv('GameResults.csv')
            