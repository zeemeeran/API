import requests
import psycopg2
from yahoo_fin.stock_info import * 

def get_db_conn():
    conn = psycopg2.connect(host="stock-db.cdedk051ucx3.us-east-1.rds.amazonaws.com", port="5432",
                            database="stockdb", user="postgres", password="postgres")
    return conn

conn = get_db_conn()
cur = conn.cursor()
    
cur.execute("select * from stocktracking")
records = cur.fetchall()

for rec in records:
    symbol = rec[0]
    currentprice = get_live_price(symbol)
    currentprice = round(currentprice, 3)
    data = get_quote_table(symbol)
    openprice = data['Open']
 
    cur.execute('UPDATE stocktracking SET currentprice = %s, openprice = %s WHERE ticker = %s', (currentprice, openprice, symbol))
            
conn.commit()
cur.close()
conn.close()
