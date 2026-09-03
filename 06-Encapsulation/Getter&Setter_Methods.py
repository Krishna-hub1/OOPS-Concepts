class Farmer:
    def __init__(self, name, Land):
        # Private instance variables
        self.__name = name
        self.__Land = Land
    def info(self):
        print(self.__name, "owns", self.__Land, "acres of Land.")
    def getsign(self):
        if self.__Land > 0:
            print(self.__name, "Has Land.")
        else:
            print(self.__name, "Discussion about Land.")
# Getter is a method that allows you to access the value of a private variable from outside the class.
    def getLand(self):
        return self.__Land
# Setter is a method that allows you to set or update the value of a private variable.
    def setLand(self, m):
        if m>0 and m<100:
            self.__Land = m
farmer1 = Farmer("Narsaih", 100)
farmer1.getsign()
farmer1.info()
farmer2 = Farmer("BMK", 0)
farmer2.setLand(50)
farmer2.getsign()
farmer2.info()

# Getter and setter methods are used to access and modify private variables from outside the class.
# Getter is used to retrieve the value of a private variable.
# Setter is used to set or update the value of a private variable.