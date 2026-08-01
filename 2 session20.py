# task1
import requests
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
print("Status Code:", response.status_code)
posts = response.json()
print("First Post Title:", posts[0]["title"])

# task2
import requests
url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "title": "My First Post",
    "body": "Hello from Python!",
    "userId": 101
}
response = requests.post(url, json=data)
print("Status Code:", response.status_code)
print("Response JSON:")
print(response.json())

# task3
import requests
url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
users = response.json()
print("Usernames with .org email:")
for user in users:
    if user["email"].endswith(".org"):
        print(user["username"])

# task4
import requests
url = "http://www.omdbapi.com/"
params = {
    "apikey": "demo",
    "s": "Avengers"
}
response = requests.get(url, params=params)
data = response.json()
print("Total Results:", data.get("totalResults"))

