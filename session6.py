# task 1
# insta_followers={
#     "virat":270000000,
#     "carryminati":2100000000,
#     "mrbeast":70000000,
#     "aliabhat":8600000,
#     "shradakapoor":9500000
# }
# print(insta_followers)

# task 2
# insta_followers["narendra modi"]=100000000   (add)
# insta_followers["virat"]=275000000   (update)
# del insta_followers["mrbeast"]    (delete)
# print(insta_followers)

# task 3
# food_prices = {
#     "Pizza": 350,
#     "Burger": 180,
#     "Biryani": 250,
#     "Pasta": 220,
#     "Sandwich": 150
# }
# print("Items costing more than ₹200:")
# for item, price in food_prices.items():
#     if price > 200:
#         print(item, ":", price)

# task 4
# flipkart_users = {"Aman", "Riya", "Karan", "Priya", "Rahul"}
# myntra_users = {"Riya", "Rahul", "Simran", "Neha", "Karan"}
# common_users = flipkart_users.intersection(myntra_users)
# print("Users on both platforms:")
# print(common_users)

# task 5
# def get_unique_artists(spotify_playlist1, spotify_playlist2):
#     return spotify_playlist1.union(spotify_playlist2)
# playlist1 = {"Arijit Singh", "Shreya Ghoshal", "Atif Aslam"}
# playlist2 = {"Atif Aslam", "KK", "Neha Kakkar"}
# unique_artists = get_unique_artists(playlist1, playlist2)
# print("Unique Artists:")
# print(unique_artists)