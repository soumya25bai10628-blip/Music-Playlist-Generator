import os
import random

FILE_NAME = "songs.txt"

if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w"):
        pass


def load_songs():
    songs = []
    with open(FILE_NAME, "r") as f:
        for line in f:
            line = line.strip()
            if line != "":
                songs.append(line.split(","))
    return songs


def save_songs(songs):
    with open(FILE_NAME, "w") as f:
        for song in songs:
            f.write(song[0] + "," + song[1] + "," + song[2] + "," + song[3] + "\n")


def add_song():
    print("\nAdd New Song")
    name = input("Song name: ")
    artist = input("Artist: ")
    mood = input("Mood (happy/sad/chill): ")
    fav = input("Favorite? (yes/no): ").lower()

    with open(FILE_NAME, "a") as f:
        f.write(name + "," + artist + "," + mood + "," + fav + "\n")

    print("Song added ^_^\n")


def view_songs():
    songs = load_songs()

    if len(songs) == 0:
        print("No songs found.\n")
        return

    print("\nAll Songs:")
    i = 1
    for song in songs:
        name = song[0]
        artist = song[1]
        mood = song[2]
        fav = song[3]

        if fav == "yes":
            tag = "^_^"
        else:
            tag = ""

        print(str(i) + ". " + name + " - " + artist + " (" + mood + ") " + tag)
        i += 1

    print()


def generate_playlist():
    songs = load_songs()
    mood_choice = input("Enter mood: ")

    playlist = []

    for song in songs:
        if song[2].lower() == mood_choice.lower():
            playlist.append(song)

    if len(playlist) == 0:
        print("No songs for this mood.\n")
        return

    random.shuffle(playlist)

    print("\nPlaylist for " + mood_choice + ":")
    i = 1
    for song in playlist:
        print(str(i) + ". " + song[0] + " - " + song[1])
        i += 1

    print()


def delete_song():
    songs = load_songs()

    if len(songs) == 0:
        print("Nothing to delete.\n")
        return

    view_songs()

    try:
        n = int(input("Enter number to delete: "))
        songs.pop(n - 1)
        save_songs(songs)
        print("Deleted ^_^\n")
    except:
        print("Invalid input.\n")


def show_favorites():
    songs = load_songs()
    favs = []

    for song in songs:
        if song[3] == "yes":
            favs.append(song)

    if len(favs) == 0:
        print("No favorite songs.\n")
        return

    print("\nFavorite Songs:")
    i = 1
    for song in favs:
        print(str(i) + ". " + song[0] + " - " + song[1] + " (" + song[2] + ") ^_^")
        i += 1

    print()


def menu():
    while True:
        print("=== Music Playlist Generator ===")
        print("1. Add Song")
        print("2. View Songs")
        print("3. Playlist by Mood")
        print("4. Delete Song")
        print("5. Favorites")
        print("6. Exit")

        choice = input("Choose: ")
        if choice == "1":
            add_song()
        elif choice == "2":
            view_songs()
        elif choice == "3":
            generate_playlist()
        elif choice == "4":
            delete_song()
        elif choice == "5":
            show_favorites()
        elif choice == "6":
            print("Goodbye ^_^")
            break
        else:
            print("Try again.\n")

menu()