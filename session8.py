# task 1
# apps = ["Zomato", "Swiggy", "Uber Eats", "Domino's", "EatSure"]
# for app in apps:
#     print(app)

# task2
# steps = [6500, 7800, 9200, 10500, 11000, 9800, 12000]
# days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# i = 0
# while i < len(steps):
#     if steps[i] > 10000:
#         print("First day crossing 10,000 steps:", days[i])
#         break
#     i += 1 

# task3
# def long_team_names(teams):
#     for team in teams:
#         if len(team) <= 6:
#             continue
#         print(team)
# ipl_teams = [
#     "CSK",
#     "RCB",
#     "Mumbai Indians",
#     "Sunrisers Hyderabad",
#     "Rajasthan Royals",
#     "Punjab Kings"
# ]

# task4
# song_durations = [210, 180, 240, 195, 225]

# for position, duration in enumerate(song_durations, start=1):
#     print(f"Song {position}: {duration} seconds")

# task5
# prices = [450, 700, 0, 600, 500, 300, 400]
# total = 0
# for price in prices:
#     if price == 0:
#         continue      # Skip out-of-stock item
#     total += price
#     if total > 2000:
#         print("Total crossed ₹2000.")
#         break         # Stop adding more items
# print("Final Total: ₹", total)
