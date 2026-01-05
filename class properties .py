"""
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def myfunc (self):
        print("Hello my name is" + self.name)

p1=Person("ZA",23)


p1.age = 56
print (p1.age)


#delete class properties

class Person:
    def __init__ (self,name,age):
        self.name= name
        self.age =age

    def myfunc(self):
        print("Hello, my name is" + self.name)

p1=Person("AL",23)
del p1.age

print(p1.name)
print(p1.age)
  

#Class properties vs instance proeperties

class Person:
    species = "Human"

    def __init__(self,name):
        self.name= name     

p1=Person("ZA")
p2 = Person ("RA")

print(p1.name)
print(p2.name)

print(p1.species)
print(p2.species)

"""

#modifying class properties

class Person:
    lastname = ""

    def __init__ (self,name):
        self.name = name

p1= Person ("Mili")
p2= Person("Lua")

Person.lastname= "Rasel"

print(p1.lastname)
print(p2.lastname)
