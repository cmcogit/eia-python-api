import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

us_input_file = requests.get("http://api.eia.gov/series/?api_key=e2815357db5ba9ad7c6f782dd01b8be9&series_id=COAL.COST.US-10.Q").json()
va_input_file = requests.get("http://api.eia.gov/series/?api_key=e2815357db5ba9ad7c6f782dd01b8be9&series_id=COAL.COST.VA-10.Q").json()
mt_input_file = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MT&apikey=2GHJ6S64A86XPK88").json()
# data = json.loads(mt_input_file)
print(type(mt_input_file['Meta Data']))
data = json.dumps(mt_input_file)
print(type(data))
# Time Series (Daily)
for time_series in mt_input_file:
    print(time_series)

serialized_us = [] # US coal quarterly cost
serialized_va = [] # VA coal quarterly cost
serialized_mt = [] # ArcelorMittal NYSE close daily
us_cost = []
va_cost = []
quarter = []
mt_close = []

# for daily in mt_input_file['Time Series (Daily)']:
#     print(daily['4. close'])

for e in us_input_file['series'][0]['data']:
    e.append(us_input_file['series'][0]['series_id'])
    serialized_us.append(e)

for e in va_input_file['series'][0]['data']:
    e.append(va_input_file['series'][0]['series_id'])
    serialized_va.append(e)

for item in serialized_us:
    us_cost.append(item[1])

for item in serialized_va:
    va_cost.append(item[1])

for item in serialized_us:
    quarter.append(item[0])



# df = pd.DataFrame(input_file['series'][0]['data'])
# df.columns = ['Q', '$/short ton', 'series_id']
# df.to_excel("quarterly_coal_short_ton.xlsx")
# making change from macbook


# plt.plot(quarter, us_cost, color='g', label='US Line')
# plt.plot(quarter, va_cost, color='b', label='VA Line')
# plt.xlabel('Quarter')
# plt.ylabel('$/short ton')
# plt.legend()
# plt.show()
