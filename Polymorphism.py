"""
x=("Apple","banana","cherry")
print(len(x))

#2
x= "Hello World"
print(len(x))

#3
class animal:
    def sound(self):
        print("Animal makes Sounds")

class dog(animal):
    def sound(self):
        print ("dog Barks")

class cat(animal):
    def sound(self):
        print("cat meows")

a=animal()
d=dog()
c=cat()

a.sound()
d.sound()
c.sound()

thisdict= {
    "brand": "Toyota",
    "model":"corola",
    "year" : 2020

}

print(len(thisdict))

#Different classes with the same method:

class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def move(self):
        print("Drive!")
class Boat:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def move(self):
        print("Sail!")

class Plane:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def move(self):
        print("Fly!")

car1= Car("Ford","Toyota")
boat1=Boat("Titanic","Tous23")
plane1=Plane("Boeing","747")
 
for x in (car1,boat1,plane1):
    x.move()
"""
#Create a class called Vehicle and make Car, Boat, Plane child classes of Vehicle

class Vechicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def move(self):
        print("Move!")
class Car(Vechicle):
    pass

class Boat(Vechicle):
    def move(self):
        print("Sail!")

class Plane(Vechicle):
    def move(self):
        print("Fly!")

car1=Car("Ford","Mustang")
boat1=Boat("Ibiza","Touring")
plane1=Plane("boeing","747")


for x in (car1,boat1,plane1):
    print(x.brand)
    print(x.model)
    x.move()
   