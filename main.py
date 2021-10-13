import pandas as pd
import datetime

def parseMonth(month):
    d = datetime.datetime.strptime(month, '%b %Y')
    if (d.month == 12):
        d = d.replace(year=d.year+1,month=1)
    else:
        d = d.replace(month=d.month+1)
    return d - datetime.timedelta(days=1)

list = ['https://www.indexmundi.com/commodities/?commodity=hard-sawn-wood',
'https://www.indexmundi.com/commodities/?commodity=hard-sawn-wood',
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

for url in list:
    tables = pd.read_html(url)

    table = tables[1]
    
    table['Month'] = table['Month'].transform(parseMonth)
    table = table.sort_values(by = 'Month', ascending = False)
    print(table)

    df = df.append(table)

df.to_csv('result.csv', columns = ['Month', 'Price'], index=False)
