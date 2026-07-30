# task1
def calculate_final_price(price, discount_rate):
    final_price = price - (price * discount_rate / 100)
    return final_price
# Example
print(calculate_final_price(1000, 20))

# task2
def get_delivery_charge(amount, city="Ahmedabad"):
    if city == "Ahmedabad":
        return 0
    else:
        return 50
# Example
print(get_delivery_charge(500))
print(get_delivery_charge(500, "Surat"))

# task3
def format_price(price, currency="INR"):
    if currency == "INR":
        return f"₹{price}"
    elif currency == "USD":
        return f"${price}"
# Example
print(format_price(500))
print(format_price(500, "USD"))

# task4
def apply_coupon(price, coupon_code=None):
    if coupon_code == "ZOMATO10":
        return price - (price * 10 / 100)
    else:
        return price
# Example
print(apply_coupon(1000))
print(apply_coupon(1000, "ZOMATO10"))