# task1
import requests
API_KEY = "YOUR_API_KEY"
CITY = "Ahmedabad"
url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    temperature = data["main"]["temp"]
    weather = data["weather"][0]["description"]
    print("Current Weather")
    print("----------------")
    print("City:", CITY)
    print("Temperature:", temperature, "°C")
    print("Weather:", weather)
except requests.exceptions.RequestException as e:
    print("Error:", e)

# task2
import requests
from datetime import datetime
url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    print("Crypto Prices")
    print("---------------------------")
    print("Date & Time:", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
    print("Bitcoin : $", data["bitcoin"]["usd"])
    print("Ethereum: $", data["ethereum"]["usd"])
except requests.exceptions.RequestException as e:
    print("Error:", e)

# task3
import requests
API_KEY = "DEMO_KEY"
url = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"
try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    print("Title:")
    print(data["title"])
    print("\nExplanation:")
    print(data["explanation"])
    image_url = data["url"]
    image = requests.get(image_url)
    with open("apod.jpg", "wb") as file:
        file.write(image.content)
    print("\nImage saved as apod.jpg")
except requests.exceptions.RequestException as e:
    print("Error:", e)

# TASK 4 AND 5 (DOUBT)
