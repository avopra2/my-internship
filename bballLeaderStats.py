from cgitb import html
from lib2to3 import refactor
import requests
from bs4 import BeautifulSoup
import pandas as pd
import argparse

url = 'https://www.basketball-reference.com/leagues/NBA_2022_leaders.html'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')
 
urls = []
refs = []
for link in soup.find_all('a'):
    ref = link.get('href')
    if ref[:8] == '/players' and ref not in refs and len(ref)>10:
        refs.append(ref)
        urls.append('https://www.basketball-reference.com' + ref)

data = {
    "Season": [],
    "Age": [],
    "Tm": [],
    "Lg": [],
    "Pos": [],
    "G": [],
    "GS": [],
    "MP": [],
    "FG": [],
    "FGA": [],
    "FG%": [],
    "3P": [],
    "3PA": [],
    "3P%": [],
    "2P": [],
    "2PA": [],
    "2P%": [],
    "eFG%": [],
    "FT": [],
    "FTA": [],
    "FT%": [],
    "ORB": [],
    "DRB": [],
    "TRB": [],
    "AST": [],
    "STL": [],
    "BLK": [],
    "TOV": [],
    "PF": [],
    "PTS": []
}

df = pd.DataFrame(data)

for plref in urls:
    tables = pd.read_html(plref)
    if len(tables) == 0:
        continue
    table = tables[0]

    df = df.append(table)

df = df.drop(df.columns[[6, 7, 9, 11, 12, 13, 14, 15, 16, 17, 19, 21, 22, 27, 28]], axis = 1)
df = df.dropna()

parser = argparse.ArgumentParser()
parser.add_argument('--csv', action = 'store', required=False)
parser.add_argument('--xlsx', action = 'store', required=False)
args = parser.parse_args()

if args.csv != None:
    df.to_csv(args.csv, index=False)

