import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from datetime import date
from dateutil.relativedelta import relativedelta

# Get todays date
# --------------------------------------------------------------------------------
# today = date.today()
# print("Today: " + str(today))

# one_yr_from_today = date(2019,5,18) + relativedelta(years=1)
# print("One year from today: " + str(one_yr_from_today))

# ten_yrs_ago = date.today() - relativedelta(years=10)
# print("Ten years ago from today: " + str(ten_yrs_ago))
# --------------------------------------------------------------------------------


# Working on getting a function built
# and takes in 6 stocks and outputs the qtr data
# --------------------------------------------------------------------------------
# Update excel with Metal Stock's
def get_metal_stocks_q1(m_1):
    month_cost = []
    serialized_list = []
    quarter = 1
    input_file = requests.get(m_1).json()
    nested_dict = input_file['Monthly Time Series']

    for month in nested_dict:
        serialized_list = {quarter:{month:nested_dict[month]['4. close']}}
        month_cost.append(serialized_list)
    print(month_cost)
    # mt_qtr1_close = {}

    # for date in mt_nested_dict:
    #     if date >= '2018-01-01' and date <= '2018-04-30':
    #         qtr1_data = {date:mt_nested_dict[date]['4. close']}
    #         mt_qtr1_close.update(qtr1_data)
    # print(mt_qtr1_close)

    # for e in mt_qtr1_close:
    #     print(e)



arcelor_mittle = "https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=MT&apikey=2GHJ6S64A86XPK88"

get_metal_stocks_q1(arcelor_mittle)
# --------------------------------------------------------------------------------


# US stuff
# --------------------------------------------------------------------------------
# us_input_file = requests.get("http://api.eia.gov/series/?api_key=e2815357db5ba9ad7c6f782dd01b8be9&series_id=COAL.COST.US-10.Q").json()
# serialized_us = [] # US coal quarterly cost
# us_cost = []

# for e in us_input_file['series'][0]['data']:
#     e.append(us_input_file['series'][0]['series_id'])
#     serialized_us.append(e)
# print(serialized_us)

# for item in serialized_us:
#     us_cost.append(item[1])

# for item in serialized_us:
#     quarter.append(item[0])
# --------------------------------------------------------------------------------


# VA stuff
# --------------------------------------------------------------------------------
# va_input_file = requests.get("http://api.eia.gov/series/?api_key=e2815357db5ba9ad7c6f782dd01b8be9&series_id=COAL.COST.VA-10.Q").json()
# va_cost = []
# serialized_va = [] # VA coal quarterly cost

# for e in va_input_file['series'][0]['data']:
#     e.append(va_input_file['series'][0]['series_id'])
#     serialized_va.append(e)

# for item in serialized_va:
#     va_cost.append(item[1])
# --------------------------------------------------------------------------------


# serialized_mt = [] # ArcelorMittal NYSE close daily


# quarter = []
# mt_qtr1_close = []

# mt_nested_dict = mt_input_file['Monthly Time Series']

# for date in mt_nested_dict:
#     if date >= '2018-01-01' and date <= '2018-04-30':
#         qtr1_data = {date:mt_nested_dict[date]['4. close']}
#         mt_qtr1_close.append(qtr1_data)
#         # mt_qtr1_close.append(mt_nested_dict[date]['4. close'])

# for e in mt_qtr1_close:
#     print(e)

# print(mt_qtr1_close[0]['2018-04-30'])

    # print(mt_nested_dict[date]['4. close'])
    # mt_cost = {date:mt_nested_dict[date]['4. close']}
    # mt_nested_dict.update(d)


# df = pd.DataFrame(serialized_us)
# df.columns = ['Q', '$/short ton', 'series_id']
# df.to_excel("quarterly_coal_short_ton.xlsx")


# plt.plot(quarter, us_cost, color='g', label='US Line')
# plt.plot(quarter, va_cost, color='b', label='VA Line')
# plt.xlabel('Quarter')
# plt.ylabel('$/short ton')
# plt.legend()
# plt.show()
