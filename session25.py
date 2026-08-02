# step1
# import requests
# import json
# import schedule
# import time

# Explanation:
# requests → Fetch data from Binance API
# json → Save and load JSON data
# schedule → Run the script every hour
# time → Used for delays and retry logic


# step2
# url = "https://api.binance.com/api/v3/ticker/24hr"
# This API returns 24-hour statistics for all cryptocurrencies

# step3
# response = requests.get(url)
# if response.status_code == 200:
#     data = response.json()
#     print("Data fetched successfully")
# else:
#     print("Error:", response.status_code)

# step4
# with open("crypto_data.json", "w") as file:
#     json.dump(data, file, indent=4)

# print("Data saved in crypto_data.json")
# This saves the complete API response

# step5
# with open("crypto_data.json", "r") as file:
#     data = json.load(file)

# step6
# def find_most_volatile_coin(data):
#     highest_change = 0
#     coin_name = ""
#     for coin in data:
#         change = abs(float(coin["priceChangePercent"]))
#         if change > highest_change:
#             highest_change = change
#             coin_name = coin["symbol"]
#     return coin_name

# step7
# total_price = 0
# for coin in data:
#     total_price += float(coin["lastPrice"])
# average_price = total_price / len(data)
# print("Average Price:", average_price)

# step8
# DOUBT