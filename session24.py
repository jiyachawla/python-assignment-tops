# step1
# import requests
# import csv
# Explanation:
# requests → Used to call the API
# csv → Used to save data into a CSV file

# step2
# url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1"
# Explanation:
# This URL fetches the Top 10 cryptocurrencies by market capitalization

# step3
# response = requests.get(url)
# Explanation:
# This sends a request to the CoinGecko API.

# step4
# if response.status_code == 200:
#     data = response.json()
# Explanation:
# status_code == 200 means the request was successful
# response.json() converts JSON data into a Python list

# step5
# for coin in data:
#     print("Name:", coin["name"])
#     print("Current Price (USD):", coin["current_price"])
#     print()

# step6
# for coin in data:
#     print("Name:", coin["name"])
#     print("Current Price:", coin["current_price"])
#     print("24h Price Change %:", coin["price_change_percentage_24h"])
#     print("24h High:", coin["high_24h"])
#     print("24h Low:", coin["low_24h"])
#     print("-" * 40)

# step7
# with open("crypto_prices.csv", "w", newline="", encoding="utf-8") as file:
# writer = csv.writer(file)
#     writer.writerow([
#         "Name",
#         "Current Price",
#         "24h Change %",
#         "24h High",
#         "24h Low"
#     ])
#     for coin in data:
#         writer.writerow([
#             coin["name"],
#             coin["current_price"],
#             coin["price_change_percentage_24h"],
#             coin["high_24h"],
#             coin["low_24h"]
#         ])
# print("Data saved successfully in crypto_prices.csv")

# step8
# DOUBT