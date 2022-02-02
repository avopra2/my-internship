import pandas as pd
import datetime
import argparse


def parseMonth(month):
    d = datetime.datetime.strptime(month, '%b %Y')
    if (d.month == 12):
        d = d.replace(year=d.year+1,month=1)
    else:
        d = d.replace(month=d.month+1)
    return d - datetime.timedelta(days=1)


parser = argparse.ArgumentParser()
parser.add_argument('--csv', action = 'store', required=False)
parser.add_argument('--xlsx', action = 'store', required=False)

args = parser.parse_args()

l = ['https://www.indexmundi.com/commodities/?commodity=hard-sawn-wood',
'https://www.indexmundi.com/commodities/?commodity=hard-logs',
'https://www.indexmundi.com/commodities/?commodity=plywood',
'https://www.indexmundi.com/commodities/?commodity=soft-logs',
'https://www.indexmundi.com/commodities/?commodity=soft-sawn-wood',
'https://www.indexmundi.com/commodities/?commodity=rock-phosphate',
'https://www.indexmundi.com/commodities/?commodity=potassium-chloride',
'https://www.indexmundi.com/commodities/?commodity=triple-superphosphate']

data = {
    "Month": [],
    "Price": [],
    "Change": []
}

df = pd.DataFrame(data)

for url in l:
    tables = pd.read_html(url)
    table = tables[1]
    
    table['Month'] = table['Month'].transform(parseMonth)
    table = table.sort_values(by = 'Month', ascending = False)
    print(table)

    df = df.append(table)

if args.csv != None:
    df.to_csv(args.csv, columns = ['Month', 'Price'], index=False)
if args.xlsx != None:
    df.to_excel(args.xlsx, columns = ['Month', 'Price'], index=False)
