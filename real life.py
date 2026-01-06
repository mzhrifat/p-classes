class Student:
    def __init__(self,name,roll,marks):
        self.name=name
        self.roll=roll
        self.marks=marks

    def get_info(self):
        return f"Name:{self.name},Roll:{self.roll},Marks={self.marks}"
    
    def is_pass(self):
        if self.marks >=40:
           return "status:Passed"
        else:
         return "status: Failed"

s1=Student("AL",200,56)
s2=Student("DA",34,39)

print(s1.get_info())
print(s1.is_pass())

print(s2.get_info())
print(s2.is_pass())
    
