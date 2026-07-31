# task1
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_discounted_price(self):
        return self.price - (self.price * 0.10)
# Object
p1 = Product("Shoes", 2000)
print("Product Name:", p1.name)
print("Discounted Price:", p1.get_discounted_price())

# task2
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def get_discounted_price(self):
        return self.price - (self.price * 0.10)
class Electronics(Product):
    def get_discounted_price(self):
        return self.price - (self.price * 0.20)
# Object
e1 = Electronics("Laptop", 50000)
print("Electronics Name:", e1.name)
print("Discounted Price:", e1.get_discounted_price())

# task3
# DOUBT

# task4
class Ticket:
    def __init__(self, movie_name, price):
        self.movie_name = movie_name
        self.price = price
    def get_final_price(self):
        return self.price
class PremiumTicket(Ticket):
    def get_final_price(self):
        return super().get_final_price() + 50
# Objects
t1 = Ticket("Avengers", 250)
t2 = PremiumTicket("Avengers", 250)
print("Normal Ticket Price:", t1.get_final_price())
print("Premium Ticket Price:", t2.get_final_price())