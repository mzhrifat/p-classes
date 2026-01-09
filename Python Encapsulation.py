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


#Use encapsulation to protect and validate data

class Person:
    def __init__(self,name):
        self.name=name
        self.__grade=0

    def set_grade(self,grade):
        if 0<=grade <=100:
            self.__grade=grade
        else:
            print("Grade must be between 0 and 100")

    def get_grade(self):
            return self.__grade

    def get_status(self):
            if self.__grade >= 60:
                return "Paseed"
            else:
                return "Failed"

student = Person("Emi")
student.set_grade(85)

print(student.get_grade())
print(student.get_status())

"""

#Create a protected property:
class Person:
    def __init__(self,name,salary):
        self.name=name
        self._salary = salary
        
p1=Person("DA",45777)
print(p1.name)
print(p1._salary)