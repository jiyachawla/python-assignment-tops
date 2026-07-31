# task1
import re

text = """
Call me at +91-9876543210 or +91-9123456789.
Office: +91-9988776655
Invalid: 9876543210
"""
pattern = r"\+91-\d{10}"
numbers = re.findall(pattern, text)
print("Phone Numbers Found:")
print(numbers)

# task2
import re
def contains_date(text):
    pattern = r"\b\d{2}/\d{2}/\d{4}\b"
    return re.search(pattern, text) is not None
print(contains_date("Meeting on 15/08/2026"))   # True
print(contains_date("Meeting tomorrow"))        # False

# task3
import re
text = """
Pizza: Rs. 299
Burger: Rs. 150
Cold Drink: Rs. 80
Cake: Rs. 1500
"""
prices = re.findall(r"Rs\.\s*(\d+)", text)
prices = [int(price) for price in prices]
print("Prices:", prices)
print("Total =", sum(prices))

# task4
import re
text = """
Contact us at support@gmail.com or help123@yahoo.com.
"""
pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
result = re.sub(pattern, "[hidden email]", text)
print(result)

# task5
import re
with open("comments.txt", "r") as file:
    text = file.read()
pattern = r"@[A-Za-z0-9_]{3,}"
usernames = re.findall(pattern, text)
unique_usernames = sorted(set(usernames))
print("Unique Instagram Usernames:")
for username in unique_usernames:
    print(username)