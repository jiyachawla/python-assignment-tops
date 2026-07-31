# task1
def get_song_duration_per_minute(total_duration, number_of_songs):
    try:
        average = total_duration / number_of_songs
        print("Average duration per song:", average, "minutes")
    except ZeroDivisionError:
        print("Error: Number of songs cannot be zero.")
    finally:
        print("Calculation completed.")
# Example
get_song_duration_per_minute(60, 12)
get_song_duration_per_minute(60, 0)

# task2
try:
    total_amount = float(input("Enter total cart amount: "))
    item_count = int(input("Enter number of items: "))
    price_per_item = total_amount / item_count
    print("Price per item:", price_per_item)
except ZeroDivisionError:
    print("Item count cannot be zero. Please enter at least 1 item.")

# task3
class NoOffersApplied(Exception):
    pass

try:
    total_spend = float(input("Enter total spend: "))
    offers = int(input("Enter number of offers applied: "))
    if offers == 0:
        raise NoOffersApplied("No offers applied. Cashback cannot be calculated.")
    average_cashback = total_spend / offers
    print("Average cashback per offer:", average_cashback)
except NoOffersApplied as e:
    print(e)

# task4
def calculate_average_rating(total_rating, num_reviews):
    try:
        return total_rating / num_reviews
    except ZeroDivisionError:
        return "Error: Number of reviews cannot be zero."
    finally:
        print("Thank you for using the calculator")
print(calculate_average_rating(500, 0))

# task5
def safe_divide_for_zomato(bill_amount, number_of_people):
    try:
        result = bill_amount / number_of_people
    except ZeroDivisionError:
        print("Error: Number of people cannot be zero.")
    else:
        print("Each person should pay:", result)
    finally:
        print("Split calculation done")
# Example
safe_divide_for_zomato(1200, 4)
print()
safe_divide_for_zomato(1200, 0)
