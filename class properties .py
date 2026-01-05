class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def myfunc (self):
        print("Hello my name is" + self.name)

p1=Person("ZA",23)


p1.age = 56
print (p1.age)
        