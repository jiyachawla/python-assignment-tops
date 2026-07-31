# task1
apps = ["Zomato", "Swiggy", "Domino's", "Uber Eats", "Pizza Hut"]
app_iterator = iter(apps)
print(next(app_iterator))
print(next(app_iterator))
print(next(app_iterator))
print(next(app_iterator))
print(next(app_iterator))

# task2
def playlist_generator(songs):
    for song in songs:
        yield song
playlist = ["Shape of You", "Perfect", "Believer", "Levitating"]
for song in playlist_generator(playlist):
    print(song)

# task3
cart = ["Pizza", "Burger", "Fries", "Coke"]
for index, item in enumerate(cart, start=1):
    print(f"Item {index}: {item}")

# task4
teams = ["Mumbai Indians", "Chennai Super Kings", "Royal Challengers Bangalore", "Kolkata Knight Riders"]
points = [18, 16, 14, 12]
for team, point in zip(teams, points):
    print(f"Team: {team}, Points: {point}")

# task5
def order_id_generator():
    order_id = 1001
    while True:
        yield order_id
        order_id += 1
generator = order_id_generator()
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
