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
"""

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