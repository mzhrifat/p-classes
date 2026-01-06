"""
class Student:
    def __init__(self,name,roll,marks):
        self.name=name
        self.roll=roll
        self.marks=marks

    def get_info(self):
        return f"Name:{self.name},Roll:{self.roll},Marks={self.marks}"
    
    def is_pass(self):
        if self.marks >=40:
           return "status:Passed"
        else:
         return "status: Failed"

s1=Student("AL",200,56)
s2=Student("DA",34,39)

print(s1.get_info())
print(s1.is_pass())

print(s2.get_info())
print(s2.is_pass())
"""

#2

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        if song not in self.songs:
            self.songs.append(song)
            print(f"Added: {song}")
        else:
            print(f"{song} already exists in playlist!")

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"Removed: {song}")
        else:
            print(f"{song} not found in playlist!")

    def show_songs(self):
        if not self.songs:
            print("Playlist is empty!")
            return

        print(f"\nPlaylist '{self.name}':")
        for i, song in enumerate(self.songs, start=1):
            print(f"{i}. {song}")

    def total_songs(self):
        return len(self.songs)

    def play_song(self, song):
        if song in self.songs:
            print(f"▶ Now playing: {song}")
        else:
            print("Song not found!")

    def shuffle_playlist(self):
        random.shuffle(self.songs)
        print("Playlist shuffled 🔀")

my_playlist = Playlist("Favorites")

my_playlist.add_song("Bohemian Rhapsody")
my_playlist.add_song("Stairway to Heaven")
my_playlist.add_song("Hotel California")
my_playlist.add_song("Bohemian Rhapsody")   # duplicate check

my_playlist.show_songs()

print("\nTotal songs:", my_playlist.total_songs())

my_playlist.play_song("Hotel California")

my_playlist.shuffle_playlist()
my_playlist.show_songs()


    
