# task1
import requests
url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "title": "My First Post",
    "body": "This is my first API request.",
    "userId": 1
}
response = requests.post(url, json=data)
print("Status Code:", response.status_code)
print("Response JSON:")
print(response.json())

# task2
import requests
url = "https://jsonplaceholder.typicode.com/posts"
playlist_name = input("Enter Playlist Name: ")
description = input("Enter Playlist Description: ")
data = {
    "title": playlist_name,
    "body": description,
    "userId": 1
}
response = requests.post(url, json=data)
result = response.json()
print("Playlist ID:", result["id"])

# task3
import requests
url = "https://reqres.in/api/users"
data = {
    "name": "Jiya",
    "job": "Student"
}
response = requests.post(url, json=data)
result = response.json()
print("User ID:", result["id"])
print("Created At:", result["createdAt"])

# task4
import requests
import csv
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
posts = response.json()[:5]
with open("posts.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Post Title", "User ID"])
    for post in posts:
        writer.writerow([post["title"], post["userId"]])
print("Data saved successfully to posts.csv")

# task5
import requests
import json
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
posts = response.json()[:5]
with open("posts.json", "w") as file:
    json.dump(posts, file, indent=4)
print("Data saved successfully to posts.json")
