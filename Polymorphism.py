"""
x=("Apple","banana","cherry")
print(len(x))

#2
x= "Hello World"
print(len(x))
"""

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