"""
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greet(self):
    print("Hello, my name is " + self.name)

p1 = Person("Emil", 25)
p1.greet()

#self change 
class Person:
    def __init__ (myobject,name,age):
        myobject.name = name
        myobject.age = age

    def greet(Wellcome):
        print("Helo,my name is"+ Wellcome.name,age)

p1=Person("Rif")
p1= Person(32)

p1.greet()



#Access multiple properties using self

class Car:
    def __init__ (self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.brand}  {self.model }")

car1= Car ("Toyota","corola","2002")
car1.display_info()



#call one method from another method using self

class Person:
    def __init__ (self,name):
        self.name = name

    def greet (self):
        return "Hello" + self.name
     
    def welcome (self):
        meseage = self.greet()
        print(meseage + "Welcome to home")
p1=Person("ZAr")
p1.welcome()
"""

class Person:
    def __int__ (self,name):
        self.name = name

    def greet(self):
        return "Hello " + self.name
    
    def welcome(self):
        meseage = self.greet
        print(meseage + "wecome to home")

p1= Person ("Rafi")
p1.welcome()
