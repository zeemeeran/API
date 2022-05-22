import requests
import psycopg2

# url parts for fetching data using api
API_KEY = '04TP0FKBX0H35EZI'
url1 = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol='
url2 = '&interval=1min&apikey='


#conn = psycopg2.connect(host="stock-db.cdedk051ucx3.us-east-1.rds.amazonaws.com", port="5432", 
#                        database="stockdb", user="postgres", password="postgres")



def get_db_conn():
    conn = psycopg2.connect(host="stock-db.cdedk051ucx3.us-east-1.rds.amazonaws.com", port="5432",
                            database="stockdb", user="postgres", password="postgres")
    return conn

conn = get_db_conn()
cur = conn.cursor()

#cur = conn.cursor()
cur.execute("select * from stocktracking")
records = cur.fetchall()

for rec in records:
    symbol = rec[0]
    fullurl = url1 + symbol + url2 + API_KEY
    r = requests.get(fullurl)
    if (r.status_code == 200):
        print("success")

    result = r.json()

    data = result['Time Series (1min)']
    data_iter = iter(data)
    first_data = next(data_iter)
    currentprice = data[first_data]['1. open']
 
    cur.execute('UPDATE stocktracking SET currentprice = %s, openprice = %s WHERE ticker = %s', (currentprice, currentprice, symbol))
            
conn.commit()
cur.close()
conn.close()
