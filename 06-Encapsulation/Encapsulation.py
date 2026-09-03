# Implementing data and method into a single unit is called encapsulation.
#The data in object cannot be accessed or modified directly from outside the class.
# We make the data private by adding two underscores before the variable name.

class Farmer:
    def __init__(self, name, land):
        # Private instance variables
        self.__name = name
        self.__land = land
    def info(self):
        print(self.__name, "owns", self.__land, "acres of Land.")
    def getsign(self):
        if self.__land > 0:
            print(self.__name, "Has Land.")
        else:
            print(self.__name, "Has Shop.")
farmer1 = Farmer("Narsaih", 100)
farmer2 = Farmer("Balu", 0)
farmer1.info()
farmer1.getsign()
farmer2.info()
farmer2.getsign()

# Here, the Farmer class encapsulates the farmer's name and land as private instance variables. 
# Here we have defined two methods, info() and getsign(), to access and display the farmer's information.
# Here name and land are private variables, so they cannot be accessed directly from outside the class.
# Here we Implemented data and method into a single unit.