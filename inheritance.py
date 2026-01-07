"""
#Create a Parent Class
class Person:
    def __init__ (self,fname,lname):
        self.firstname=fname
        self.lastname=lname

    def printname(self):
        print(self.firstname,self.lastname)

##Use the Person class to create an object, and then execute the printname method:
x1=Person("Jo","Ha")
x1.printname()

#Create a child class

class Person:
    def __init__ (self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    
    def printname(self):
        print(self.firstname,self.lastname)
class Student(Person):
    pass

x=Student("HJ","gf")
x.printname()


#ADD a __init__ () function
class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname = lname

    def printname(self):
        print(self.firstname,self.lastname)

class Student(Person):
    def __init__(self,fname,lname):
        Person.__init__(fname,lname)

x=Student("MIKe","Koly")
x.printname()
 """

 #add a super() function commit

class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print (self.firstname,self.lastname)
    
class Student(Person):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)
x=Student("AHJ","affg")
x.printname()