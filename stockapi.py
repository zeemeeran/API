import requests

API_KEY = 'demo'
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo'


r = requests.get(url + API_KEY)
if (r.status_code == 200):
    #print(r.json())
    print("success")

result = r.json()


dataForAllDays = result['Time Series (Daily)']
dataForSingleDate = dataForAllDays['2021-12-29']
print(dataForSingleDate['1. open'])
print(dataForSingleDate['2. high'])
print(dataForSingleDate['3. low'])
print(dataForSingleDate['4. close'])
print(dataForSingleDate['5. volume'])

print(url)