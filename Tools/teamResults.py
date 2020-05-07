import requests
import lxml.html as lh
import pandas as pd
from selenium import webdriver
import time
import csv


def parse(html):
    driver = webdriver.Chrome()
    driver.get(html)
    time.sleep(5)
    source_code = driver.page_source
    return source_code


data = [('Year', [])]
options = webdriver.ChromeOptions()
options.add_argument('headless')

for year in range(1996, 2019):
    next_yr = (year % 100) + 1
    if next_yr == 100:
        next_yr = 0

    if next_yr < 10:
        next_yr = '0' + str(next_yr)

    url = 'https://stats.nba.com/teams/traditional/?sort=TEAM_NAME&dir=1&Season=' + str(year) + '-' + str(next_yr) + \
          '&SeasonType=Regular%20Season&PerMode=PerMinute'
    page = parse(url)

    # Store the contents of the website under doc
    doc = lh.fromstring(page)

    # Find the table row elements
    tr_elements = doc.xpath('//tr')
    # Take the first year of data and use it to get the headers of the table columns
    k = 0
    if year == 1996:
        for t in tr_elements[0]:
            # Exclude first column because there's no info
            if 0 < k < 28:
                headers = t.text_content()
                data.append((headers, []))
            k += 1

    for i in range(1, len(tr_elements)):
        row = tr_elements[i]

        # Check that we're pulling data from the tables we want, and not other tr elements
        if len(row) != 28:
            break

        j = 0
        for cell in row.iterchildren():
            # Grab data from each cell in each row, and convert to float if possible
            info = cell.text_content()
            # Year was not originally a column, so manually add the year since we're pulling from mult. tables
            if j == 0:
                data[j][1].append(year)
            elif j > 0:
                try:
                    converted = float(info)
                    data[j][1].append(converted)
                except ValueError:
                    converted = info.strip('\n')
                    converted = converted.strip()
                    data[j][1].append(converted)
                    pass
            j += 1

# Create pandas data-frame
dictionary = {title: column for (title, column) in data}
df = pd.DataFrame(dictionary)
df.to_csv("TeamStats.csv")
