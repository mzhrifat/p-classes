"""
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)


class Student:
  def __init__(self, name, age=18):
    self.name = name
    self.age = age

p1 = Student("Emil")
p2 = Student("Tobias", 25)


print(p1.name,p1.age)
print(p2.name,p2.age)
"""

class Person:
    def __init__(self,name,age,city,country):
     self.name = name  
     self.age = age
     self.city = city
     self.country = country

s1=Person("Rif",22,"Dhaka","Norway")   

print(s1.name)
print(s1.age)
print(s1.city)
print(s1.country)