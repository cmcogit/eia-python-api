import requests
import json
import pandas as pd
import matplotlib.pyplot as plt

us_input_file = requests.get("http://api.eia.gov/series/?api_key=e2815357db5ba9ad7c6f782dd01b8be9&series_id=COAL.COST.US-10.Q").json()
va_input_file = requests.get("http://api.eia.gov/series/?api_key=e2815357db5ba9ad7c6f782dd01b8be9&series_id=COAL.COST.VA-10.Q").json()

serialized_us = []
serialized_va = []
us_cost = []
va_cost = []
quarter = []

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
# test


plt.plot(quarter, us_cost, color='g')
plt.plot(quarter, va_cost, color='b')
# plt.plot(quarter, us_cost, color='orange')
# plt.plot(us_cost)
# plt.ylabel('some numbers')
plt.show()
# print(df.head(5))

# print(plot_list)