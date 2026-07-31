# task1
import math
result = math.sqrt(225)
print("Square root of 225 is:", result)

# task2
import os
folder_name = "MyDownloads"
os.makedirs(folder_name, exist_ok=True)
print("Folder created at:")
print(os.path.abspath(folder_name))

# task3
from datetime import datetime
current_time = datetime.now()
formatted_time = current_time.strftime("%d-%m-%Y %H:%M:%S")
print("Current Date and Time:", formatted_time)

# task4
# import playlist_utils

# playlist = []

# playlist_utils.add_song(playlist, "Shape of You")
# playlist_utils.add_song(playlist, "Believer")
# playlist_utils.add_song(playlist, "Perfect")

# print("Final Playlist:")
# print(playlist)

# task5
# DOUBT