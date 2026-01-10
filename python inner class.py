"""

class Outer:
    def __init__(self):
        self.name="Outer"
    
    class Inner:
        def __init__(self):
            self.name = "Inner Class"
        
        def display(self):
            print("This is the inner class")

outer= Outer()
inner = outer.Inner()
inner.display()


#Pass the outer class instance to the inner class
class Outer:
    def __init__(self):
        self.name = "Emil"

    class Inner:
        def __init__(self,outer):
            self.outer = outer

        def display(self):
             print(f"Outer class name: {self.outer.name}")

outer = Outer()
inner = outer.Inner(outer)
inner.display()
"""

#Use an inner class to represent a car's engine
class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        self.engine = self.Engine()

    class Engine():
        def __init__(self):
            self.status = "Off"
        
        def start(self):
            self.status = "Running"
            print("Engine Started")

        def stop(self):
            self.status = "Off"
            print("Engine stoppers")

    
    def drive(self):
        if self.engine.status == "Running":
            print (f"Driving the {self.brand} {self.model}")

        else:
            print("start the engine first")
car= Car("BMW","Ford")
car.drive()
car.engine.start()
car.drive()
