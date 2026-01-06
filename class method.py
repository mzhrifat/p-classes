"""
class Person:
    def __init__(self,name):
        self.name=name

    def greet(self):
        print("Hello,my name is " + self.name)

p1=Person("Emi")
p1.greet()

#make a calculator

class Calculator:
    def add(self,a,b):
        return a+b
    
    def multiply(self,a,b):
        return a*b

calc= Calculator()
print(calc.add(10,4))
print(calc.multiply(6,5))


#Methods Accessing Properties
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def get_info(self):
        return  f"{self.name} is {self.age} years old"

p1=Person("AS" ,33)
print(p1.get_info())

#A method that changes a property value:

class Person:
    def __init__(self,name,age):
        self.name =name 
        self.age = age
    
    def celebrate_birthday(self):
        self.age +=1
        print (f"Happy Birthday! You are Now {self.age}")

p1=Person("DF",24)
p1.celebrate_birthday()
p1.celebrate_birthday()


#With the __str__() method:

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"{self.name} ({self.age})"

p1=Person("TO",23)
print(p1)
"""
#create a multiple methods in a class

class Playlist:
    def __init__ (self,name):
        self.name =name
        self.songs = []

    def add_song(self,song):
        self.songs.append(song)
        print (f"added : {song}")

    def remove_songs(self,song):
        if song in self.songs:
            self.songs.remove(song)
            print (f"Removed:{song}")

    def show_songs(self):
        print (f"playlist '{self.name}' :")
        for song in self.songs:
            print (f" -{song}")

my_playlist=Playlist ("Favourite")
my_playlist.add_song("AAAABC")
my_playlist.add_song("SCC")
my_playlist.show_songs()