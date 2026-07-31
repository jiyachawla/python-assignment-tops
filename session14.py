# task1
# Create and write to playlist.txt
with open("playlist.txt", "w") as file:
    file.write("Shape of You\n")
    file.write("Blinding Lights\n")
    file.write("Levitating\n")
    file.write("Perfect\n")
    file.write("Senorita\n")
print("playlist.txt created successfully!")

# task2
# Read playlist.txt and print songs in uppercase
with open("playlist.txt", "r") as file:
    for song in file:
        print(song.strip().upper())

# task3
import csv
with open("ipl_matches.csv", "r") as file:
    reader = csv.DictReader(file)
    print("Match Winners:")
    for row in reader:
        print(f"Match {row['match_id']}: {row['winner']}")

# task4
import json
with open("movies.json", "r") as file:
    movies = json.load(file)
print("Movie Ratings:")
for movie in movies:
    print(f"{movie['title']} - Rating: {movie['rating']}")

# task5
# DOUBT
