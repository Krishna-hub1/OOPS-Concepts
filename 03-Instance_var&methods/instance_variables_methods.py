class Farmer:
    def __init__(self, name, land):
        self.name = name
        self.land = land

    def display(self):
        print("Name:", self.name)
        print("land:", self.land)


farmer1 = Farmer("Balu", 22)
farmer2 = Farmer("Krishna", 21)

farmer1.display()
farmer2.display()
"""
Here we have created a class Farmer and defined a constructor __init__() that takes two parameters name and land.
Instance variables are variables that belong to a particular object. They are defined using self inside the constructor. 
In this example, name and land are instance variables
Instance methods are methods that belong to a particular object. They are defined using self as the first parameter.
"""