from yahoo_fin.stock_info import * 

print(get_live_price('FB'))
data = get_quote_table('FB')
print(data)
print(data['Open'])
