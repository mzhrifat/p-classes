"""
#Get Private Property Value

class Person:
    def __init__(self,name,age):
        self.name=name
        self.__age=age

    def get_age(self):
        return self.__age
    
p1=Person("Tobias",25)
print(p1.get_age())
"""

#Use a setter method to change a private property

class Person:
    def __init__(self,name,age):
        self.name=name
        self.__age=age

    def get_age(self):
        return self.__age
    
    def set_age(self,age):
        if age>0:
            self.__age = age
        else:
            print("Age must be positive")

p1=Person("AN",21)
print(p1.get_age())

p1.set_age(26)
print(p1.get_age())

    