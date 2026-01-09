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

#payment method

class Payment():
    def pay(self,amount):
        print("Processing Payment")

class CreditCard(Payment):
    def pay(self,amount):
        print(f"paid {amount} TK using CreditCard")

class Bkash(Payment):
    def pay(self,amount):
        print(f"paid {amount} TK using Bkash")

class Nagad():
    def pay(self,amount):
        print(f"paid{amount} TK using Nagad")

class Rocket(Payment):
    def pay(self,amount):
        print(f"paid{amount} Tk usinf Rocket")

Payments=[CreditCard(),Bkash(),Nagad(),Rocket()]
amount=100
for Payment in Payments:
    Payment.pay(amount)        

###
class Vecicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    
    def move(self):
        print("Move!")

class Car(Vecicle):
    pass

class Boat(Vecicle):
    def move (self):
       print("Sail!")

class Plane(Vecicle):
    def move(self):
        print("Fly!")

car1=Car("ca","fa")
boat1=Boat("daa","da")
plane1=Plane("ajaj","999")

for x in (car1, boat1, plane1):
   print(x.brand)
   print(x.model)
   x.move()
"""

#Use encapsulation to protect and validate data
class Person:
    def __init__(self,name):
        self.name=name
        self.__grade = 0

    def set_grade(self,grade):
        if 0<=grade <=100:
            self.__grade=grade
        else:
            print("Grade Must be between 0 and 100")

    def get_grade(self):
        return self.__grade
    
    def get_status(self):
        if self.__grade>=60:
            return "Passed"
        else:
            return "Failed"
    
student = Person("emi")
student.set_grade(85)

print(student.get_grade())
print(student.get_status())