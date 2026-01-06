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

"""
#Methods Accessing Properties
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def get_info(self):
        return  f"{self.name} is {self.age} years old"

p1=Person("AS" ,33)
print(p1.get_info())