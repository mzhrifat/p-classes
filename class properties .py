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
"""

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
        