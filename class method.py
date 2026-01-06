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
"""
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