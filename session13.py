# task1
def print_playlist_songs(songs):
    if len(songs) == 0:   # Base case
        return
    print(songs[0])       # Print first song
    print_playlist_songs(songs[1:])   # Recursive call
# Example
playlist = ["Shape of You", "Blinding Lights", "Levitating", "Senorita"]
print_playlist_songs(playlist)

# task2
def count_unread_messages(messages):
    total = messages.get("count", 0)
    for subgroup in messages.get("subgroups", []):
        total += count_unread_messages(subgroup)
    return total
# Example
chat = {
    "count": 5,
    "subgroups": [
        {
            "count": 3,
            "subgroups": []
        },
        {
            "count": 2,
            "subgroups": [
                {
                    "count": 4,
                    "subgroups": []
                }
            ]
        }
    ]
}
print("Total Unread Messages:", count_unread_messages(chat))

# task3
x = "global"
def outer():
    x = "outer"
    def inner():
        nonlocal x
        x = "inner"
    inner()
    print("Inside outer:", x)
outer()
print("Outside:", x)

# task4
def format_number_short(n):
    if n < 1000:
        return str(n)
    if n < 1000000:
        return str(round(n / 1000, 1)) + "K"
    return str(round(n / 1000000, 1)) + "M"
# Example
print(format_number_short(500))
print(format_number_short(1500))
print(format_number_short(1200000))
print(format_number_short(2500000))


