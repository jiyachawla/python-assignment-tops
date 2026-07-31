# task1
class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration
# Create an object
song1 = Song("Shape of You", "Ed Sheeran", 233)
# Print details
print("Title:", song1.title)
print("Artist:", song1.artist)
print("Duration:", song1.duration, "seconds")

# task2
class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    def play_preview(self):
        print(f"Playing 30-second preview of {self.title} by {self.artist}")
# Create object
song1 = Song("Shape of You", "Ed Sheeran", 233)
# Call method
song1.play_preview()

# task3
class FoodOrder:
    def __init__(self, restaurant_name, items, total_price):
        self.restaurant_name = restaurant_name
        self.items = items
        self.total_price = total_price
# Create object
order = FoodOrder(
    "Zomato",
    ["Pizza", "Burger"],
    550
)
# Print details
print("Restaurant:", order.restaurant_name)
print("Items:", order.items)
print("Total Price: Rs.", order.total_price)

# task4
# DOUBT


# task5
class Song:
    def __init__(self, title, artist, duration=0):
        self.title = title
        self.artist = artist
        self.duration = duration

# Object with duration
song1 = Song("Believer", "Imagine Dragons", 204)
# Object without duration
song2 = Song("Perfect", "Ed Sheeran")
print(song1.title, "-", song1.duration, "seconds")
print(song2.title, "-", song2.duration, "seconds")