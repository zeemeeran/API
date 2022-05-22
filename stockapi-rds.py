import requests
import psycopg2

API_KEY = '04TP0FKBX0H35EZI'
symbol = 'FB'
url1 = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol='
url2 = '&interval=1min&apikey='
fullurl = url1 + symbol + url2 + API_KEY

r = requests.get(fullurl)
if (r.status_code == 200):
    print("success")

result = r.json()

data = result['Time Series (1min)']
data_iter = iter(data)
first_data = next(data_iter)

#print(first_data)
currentprice = data[first_data]['1. open']

#print(fullurl)

def get_db_conn():
    conn = psycopg2.connect(host="***********************.rds.amazonaws.com", port="5432",
                            database="stockdb", user="postgres", password="postgres")
    return conn

conn = get_db_conn()
cur = conn.cursor()
cur.execute('INSERT INTO stocktracking (ticker, currentprice, openprice)'
                        'VALUES (%s, %s, %s)',
                        (symbol, currentprice, currentprice))
            
conn.commit()
cur.close()
conn.close()
