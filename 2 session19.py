# task1
import requests
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
posts = response.json()
print("First 5 Post Titles:")
for post in posts[:5]:
    print(post["title"])

# task2
import json
restaurant = {
    "name": "Spice Garden",
    "location": "Ahmedabad",
    "cuisines": ["Indian", "Chinese", "Punjabi"],
    "ratings": 4.5
}
restaurant_json = json.dumps(restaurant, indent=4)
print(restaurant_json)

# task3
import requests
url = "https://jsonplaceholder.typicode.com/posts"
playlist = {
    "title": "My Favorite Songs",
    "userId": 1,
    "body": "Shape of You, Believer, Perfect"
}
response = requests.post(url, json=playlist)
print("Status Code:", response.status_code)
print("Response JSON:")
print(response.json())

# task4
import requests
url = "https://jsonplaceholder.typicode.com/posts"
params = {
    "userId": 2
}
response = requests.get(url, params=params)
posts = response.json()
print("Post IDs by User 2:")
for post in posts:
    print(post["id"])

# task5
import requests
url = "https://jsonplaceholder.typicode.com/posts"
headers = {
    "Authorization": "Bearer my_sample_token",
    "User-Agent": "Python Requests"
}
response = requests.get(url, headers=headers)
print("Status Code:", response.status_code)