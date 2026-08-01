# task1
import requests
session = requests.Session()
url = "https://www.flipkart.com/account/orders"
response1 = session.get(url)
print("First Request Status Code:", response1.status_code)
response2 = session.get(url)
print("Second Request Status Code:", response2.status_code)
print("\nCookies Stored in Session:")
print(session.cookies.get_dict())

# explanation
# requests.Session() stores cookies between requests
# Since you're not logged in, Flipkart may redirect you to the login page
# You can observe whether cookies change after the first request

# task2
import requests
API_KEY = "YOUR_API_KEY"
url = f"https://api.openweathermap.org/data/2.5/weather?q=Ahmedabad&appid={API_KEY}&units=metric"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    temperature = data["main"]["temp"]
    print("Current Temperature in Ahmedabad:", temperature, "°C")
else:
    print("Error:", response.status_code)
    print(response.text)

# Explanation
# Sends a GET request to OpenWeatherMap
# Reads the JSON response
# Prints the current temperature in Celsius

# task3
# DOUBT

# task4
import requests
def get_user_profile():
    url = "https://jsonplaceholder.typicode.com/users/1"

    headers = {
        "Authorization": "Bearer fake_token_12345"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        user = response.json()
        print("User Name:", user["name"])
    else:
        print("Error:", response.status_code)
get_user_profile()

# explanation
# Sends an Authorization header in the format
# Authorization: Bearer fake_token_12345
# Fetches user details and prints the user's name
# JSONPlaceholder ignores the token, making it suitable for demonstrating the header format

# task5
from urllib.parse import urlencode
client_id = "YOUR_CLIENT_ID"
redirect_uri = "http://localhost:8080/callback"
params = {
    "client_id": client_id,
    "response_type": "code",
    "redirect_uri": redirect_uri,
    "scope": "user-read-email user-read-private"
}
auth_url = "https://accounts.spotify.com/authorize?" + urlencode(params)
print("Spotify OAuth Login URL:")
print(auth_url)

# Explanation:
# This code creates the first step of the OAuth 2.0 Authorization Code flow
# It builds the Spotify authorization URL with
# client_id – identifies your application
# response_type=code – requests an authorization code
# redirect_uri – where Spotify sends the user after login
# scope – specifies the permissions your application requests
# When the user opens the generated URL in a browser, they are redirected to Spotify's login page
# After logging in and granting permission, Spotify redirects them back to the specified redirect_uri 