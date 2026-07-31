# task1
class Playlist:
    def __init__(self):
        self._songs = []   # Private attribute

    def add_song(self, song):
        self._songs.append(song)

    def show_playlist(self):
        print("Playlist:", self._songs)
# Object
playlist = Playlist()
playlist.add_song("Shape of You")
playlist.add_song("Blinding Lights")
playlist.add_song("Levitating")
playlist.show_playlist()

# task2
class Product:
    def __init__(self):
        self._price = 0

    def set_price(self, price):
        self._price = price

    def get_price(self):
        return self._price
# Object
product = Product()
product.set_price(49999)
print("Product Price:", product.get_price())

# task3
class Movie:
    def __init__(self):
        self._rating = 0.0

    def set_rating(self, rating):
        if 0 <= rating <= 10:
            self._rating = rating
        else:
            print("Error: Rating must be between 0 and 10.")

    def get_rating(self):
        return self._rating
# Object
movie = Movie()
movie.set_rating(8.7)
print("Movie Rating:", movie.get_rating())
movie.set_rating(12)   # Invalid

# task4
from abc import ABC, abstractmethod

# Abstract Class
class PaymentMethod(ABC):

    @abstractmethod
    def pay(self, amount):
        pass
# Subclass 1
class Paytm(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Paytm.")
# Subclass 2
class PhonePe(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ₹{amount} using PhonePe.")

# Objects
paytm = Paytm()
phonepe = PhonePe()

paytm.pay(500)
phonepe.pay(1200)
