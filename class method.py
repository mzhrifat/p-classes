"""
class Person:
    def __init__(self,name):
        self.name=name

    def greet(self):
        print("Hello,my name is " + self.name)

p1=Person("Emi")
p1.greet()
"""
#make a calculator

class Calculator:
    def add(self,a,b):
        return a+b
    
    def multiply(self,a,b):
        return a*b

calc= Calculator()
print(calc.add(10,4))
print(calc.multiply(6,5))

